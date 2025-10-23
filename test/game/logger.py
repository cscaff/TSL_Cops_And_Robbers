# natural_logger.py
from llama_cpp import Llama

# Load once globally when module is imported
llm = Llama(
    model_path="/Users/christianscaff/Documents/Academics/Columbia/Barnard-PL-Lab/llama.cpp/llama-2-7b-chat.gguf",
    n_ctx=2048,
    n_threads=4,     # adjust for your CPU
    n_gpu_layers=0,  # set >0 if GPU acceleration is available
)

def trace_to_natural_language(formal_log: str):
    """
    Converts a formal system trace into a concise natural-language description.
    """
    prompt = f"""Translate the following formal controller trace into a clear, human-readable description:

Formal Trace:
{formal_log}

Natural Description:"""

    result = llm(prompt, max_tokens=256, stop=["\n"])
    text_output = result["choices"][0]["text"].strip()
    print(f"[NATURAL TRACE] {text_output}")
    return text_output
