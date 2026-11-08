import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_with_persona(persona, user_question):
    """Send a prompt that defines a clear persona for the model."""
    system_prompt = f"""
    You are {persona}.

    Rules:
    - Answer in a clear and helpful way.
    - Match the tone and expertise of this persona.
    - Use simple examples when explaining technical ideas.
    - Keep the response concise but complete.
    - If the question is ambiguous, ask one clarifying question before answering.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    persona = "a senior Python mentor who teaches beginners with patience and examples"
    question = "Explain the difference between a list and a tuple in Python. Give one real-life example."

    answer = ask_with_persona(persona, question)
    print("Persona-based Prompting Example\n")
    print(answer)
