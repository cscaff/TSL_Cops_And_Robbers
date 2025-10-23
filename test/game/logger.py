from openai import OpenAI
import os

OpenAI.api_key = os.getenv("OPENAI_API_KEY")


def natural_log(formal_log: str):
    response = client.responses.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that converts traces of agent behavior into concise natural language."},
            {"role": "user", "content": f"Translate this trace into a concise natural language description: {formal_log}"}
        ],
        max_tokens=100
    )

    print(response.output_text)

    return True