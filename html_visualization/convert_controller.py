#!/usr/bin/env python3
"""
Simple Python to JavaScript controller converter for Cops and Robbers game.
This script provides basic conversion of Python controller code to JavaScript.
"""

import re
import sys
import argparse


def convert_python_to_js(python_code):
    """
    Convert Python controller code to JavaScript.
    This is a basic converter that handles common patterns.
    """
    js_code = python_code

    # Convert function definition
    js_code = re.sub(r'def updateState\(_inputs_and_cells\):',
                     'function updateState(inputs) {', js_code)

    # Convert itemgetter pattern to destructuring
    # Example: currentState, Robber.x, Cop.x = itemgetter("currentState", "Robber.x", "Cop.x")(_inputs_and_cells)
    itemgetter_pattern = r'([a-zA-Z_., ]+)\s*=\s*itemgetter\((.*?)\)\(_inputs_and_cells\)'
    match = re.search(itemgetter_pattern, js_code)
    if match:
        vars_str = match.group(1)
        keys_str = match.group(2)

        # Parse variable names
        vars_list = [v.strip() for v in vars_str.split(',')]

        # Convert Cop.x, Robber.x to Cop_x, Robber_x for JS
        keys_list = [k.strip().strip('"').replace('.', '_') for k in keys_str.split(',')]

        # Create destructuring assignment
        destructure = 'const { ' + ', '.join(keys_list) + ' } = inputs;'

        # Create individual variable declarations
        var_declarations = []
        for var_name, key_name in zip(vars_list, keys_list):
            clean_var = var_name.replace('.', '_')
            if clean_var != key_name:
                var_declarations.append(f'let {clean_var} = {key_name};')

        replacement = destructure
        if var_declarations:
            replacement += '\n  ' + '\n  '.join(var_declarations)

        js_code = re.sub(itemgetter_pattern, replacement, js_code)

    # Initialize next variables
    js_code = js_code.replace('_next_Cop.x', 'next_Cop_x')
    js_code = js_code.replace('_next_Cop.y', 'next_Cop_y')
    js_code = js_code.replace('_next_Robber.x', 'next_Robber_x')
    js_code = js_code.replace('_next_Robber.y', 'next_Robber_y')

    # Add variable initializations after destructuring
    if 'next_Cop_x' in js_code:
        js_code = js_code.replace('const { ', 'const { ', 1)
        # Find the first occurrence after destructuring
        lines = js_code.split('\n')
        for i, line in enumerate(lines):
            if 'const {' in line:
                # Insert after destructuring
                lines.insert(i + 1, '  let next_Cop_x = Cop_x;')
                if 'next_Cop_y' in js_code:
                    lines.insert(i + 2, '  let next_Cop_y = Cop_y;')
                if 'next_Robber_x' in js_code:
                    lines.insert(i + 3, '  let next_Robber_x = Robber_x;')
                if 'next_Robber_y' in js_code:
                    lines.insert(i + 4, '  let next_Robber_y = Robber_y;')
                lines.insert(i + 5, '  let nextState = currentState;')
                break
        js_code = '\n'.join(lines)

    # Replace variable references
    js_code = js_code.replace('Cop.x', 'Cop_x')
    js_code = js_code.replace('Cop.y', 'Cop_y')
    js_code = js_code.replace('Robber.x', 'Robber_x')
    js_code = js_code.replace('Robber.y', 'Robber_y')

    # Replace currentState assignments
    js_code = re.sub(r'\bcurrentState\s*=', 'nextState =', js_code)

    # Convert boolean operators
    js_code = js_code.replace(' and ', ' && ')
    js_code = js_code.replace(' or ', ' || ')
    js_code = js_code.replace(' not ', ' !')
    js_code = re.sub(r'\bnot\s+', '!', js_code)

    # Convert comparison operators
    js_code = js_code.replace('==', '===')
    js_code = js_code.replace('!=', '!==')

    # Convert elif to else if
    js_code = re.sub(r'\belif\b', 'else if', js_code)

    # Process line by line to add braces
    lines = js_code.split('\n')
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        current_indent = len(line) - len(stripped)

        # Check if this is a control statement
        if re.match(r'\s*(if|else if|else)\s*[\(:]', line):
            # Remove colon and add brace
            line = line.rstrip().rstrip(':') + ' {'
            new_lines.append(line)

            # Find the block of code at the next indent level
            i += 1
            block_lines = []
            expected_indent = None

            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.lstrip()
                next_indent = len(next_line) - len(next_stripped)

                if not next_stripped:  # Skip empty lines
                    i += 1
                    continue

                if expected_indent is None:
                    expected_indent = next_indent

                # If we're at a control statement at the same or lower indent, close block
                if (next_indent <= current_indent and
                    re.match(r'\s*(if|elif|else if|else|return)\s*[\(:]', next_line)):
                    break

                # If indent decreased, close block
                if next_indent < expected_indent:
                    break

                block_lines.append(next_line)
                i += 1

            # Add block lines
            new_lines.extend(block_lines)
            new_lines.append(' ' * current_indent + '}')
            continue

        else:
            new_lines.append(line)
            i += 1

    js_code = '\n'.join(new_lines)

    # Convert return statement
    js_code = re.sub(
        r'return\s*\{\s*"currentState":\s*currentState,\s*"Cop\.x":\s*_next_Cop\.x\s*\}',
        'return { currentState: nextState, Cop_x: next_Cop_x };',
        js_code
    )
    js_code = re.sub(
        r'return\s*\{\s*"currentState":\s*nextState,\s*"Cop\.x":\s*next_Cop_x\s*\}',
        'return { currentState: nextState, Cop_x: next_Cop_x };',
        js_code
    )

    # Generic return statement conversion
    js_code = re.sub(r'return\s*\{([^}]+)\}', lambda m: convert_return_dict(m.group(1)), js_code)

    return js_code


def convert_return_dict(dict_content):
    """Convert Python dict in return statement to JS object."""
    pairs = []
    for item in dict_content.split(','):
        item = item.strip()
        if ':' in item:
            key, val = item.split(':', 1)
            key = key.strip().strip('"')
            val = val.strip()
            # Convert variable references
            val = val.replace('_next_Cop.x', 'next_Cop_x')
            val = val.replace('_next_Cop.y', 'next_Cop_y')
            val = val.replace('_next_Robber.x', 'next_Robber_x')
            val = val.replace('_next_Robber.y', 'next_Robber_y')
            val = val.replace('currentState', 'nextState')
            key = key.replace('.', '_')
            pairs.append(f'{key}: {val}')
    return 'return { ' + ', '.join(pairs) + ' };'


def main():
    parser = argparse.ArgumentParser(
        description='Convert Python controller to JavaScript for HTML visualization'
    )
    parser.add_argument('input_file', help='Input Python file (e.g., test/debugging/test.py)')
    parser.add_argument('-o', '--output', help='Output JavaScript file (default: stdout)')

    args = parser.parse_args()

    # Read Python file
    try:
        with open(args.input_file, 'r') as f:
            python_code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found", file=sys.stderr)
        sys.exit(1)

    # Extract only the updateState function
    match = re.search(r'def updateState\(_inputs_and_cells\):.*?(?=\n(?:def |class |if __name__)|\Z)',
                     python_code, re.DOTALL)

    if not match:
        print("Error: Could not find updateState function in input file", file=sys.stderr)
        sys.exit(1)

    update_state_func = match.group(0)

    # Convert to JavaScript
    js_code = convert_python_to_js(update_state_func)

    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(js_code)
        print(f"Converted controller written to {args.output}")
    else:
        print(js_code)


if __name__ == '__main__':
    main()
