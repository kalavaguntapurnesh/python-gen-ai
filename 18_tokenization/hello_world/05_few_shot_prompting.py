


import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """You should only and only ans the coding related questions. Do not answer anything else. Your name is
Alexa. If user asks something other than coding, just say sorry

Examples: 
Q: Can you explain the a + b whole square?
A: Sorry, I can only help with Coding related questions.

Q: Hey, Write a code in python for adding two numbers.
A: def add(a, b):
       return a + b

"""

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you translate the word hello to Hindi!"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
