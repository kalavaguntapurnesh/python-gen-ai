# we can use gemini inside open AI also


import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "system", "content": "You are a friendly assistant."},
        {"role": "user", "content": "Hey, I am Purnesh Kalavagunta. Nice to meet you."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
