# Securing Path
import os
import sys
    
# TSL Command
import subprocess

# REGEX
import re

# Transformer
from game.transformer import transformer


def synthesize(spec: str):
    # Connect paths
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    spec_path = os.path.join(parent_dir, 'src', spec)

    # Run the TSL synth command and capture its output
    proc = subprocess.run(
        ["issy", "--tslmt", "--solve", "--synt", spec_path],
        check=True,
        stdout=subprocess.PIPE
    )
    generated_code = proc.stdout.decode("utf-8").strip()

    # Correctly quote "CurrentState":
    pattern = re.compile(
        r'itemgetter\(\s*currentState\s*,'
    )

    generated_code = pattern.sub('itemgetter("currentState",', generated_code)

    # Strip a trailing '}' if it appears alone on its own line
    # This removes exactly one extra closing brace (and any surrounding whitespace/newlines)
    generated_code = re.sub(r"\n*\}\s*$", "", generated_code)

    return generated_code


def inject(code: str):
    # Read the target file
    BASE_DIR = os.path.dirname(__file__)
    target_path = os.path.join(BASE_DIR, "game", "controller.c")

    # Add trace logging
    # output = transformer(code)
    output = code

    # Write Back
    with open(target_path, "w") as f:
        f.write(output) 
    
    print(f"Done!\n ------- Injected updateState into {target_path}\n-------")


def trace_inject():
    # Output file
    new_text = ""
    # Read target file
    BASE_DIR = os.path.dirname(__file__)
    target_path = os.path.join(BASE_DIR, "game", "controller.c")
    with open(target_path, "r") as f:
        text = f.read()
        new_text = transformer(text)

    # Write Back
    with open(target_path, "w") as f:
        f.write(new_text) 
    

def run():
    subprocess.run(["python3", "./game/game.py"])


def main(arguments):
    if len(arguments) > 1 and arguments[1] == "-S":
        # Synth
        code = synthesize("spec.tslmt")
        # Inject
        inject(code)
        # Run
        run()
    else:
        # Run
        run()


if __name__ == '__main__':
    main(sys.argv)