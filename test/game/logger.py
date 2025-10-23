from openai import OpenAI
import os

def natural_log(formal_log: str):
    # Initialize client with API key
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Create response
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that converts traces of agent behavior into concise natural language."},
            {"role": "user", "content": f"Translate this trace into a concise natural language description as if you are the finite state machine, making a decision: {formal_log}"}
        ],
        max_tokens=100
    )

    # Print the model's reply
    print(response.choices[0].message.content)

    return True
