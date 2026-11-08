import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """

You're an expert AI Assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT

Rules: 
    - Strictly follow the given JSON output format
    - Only run one step at a time
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the display to the user).
    
    Output JSON Format:
    {"step" : "START" | "PLAN" | "OUTPUT", "content" : "string"}
    
    Example : 
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN : {"step" : "PLAN" : "content" : "Seems like user is interested in maths problem"}
    PLAN : {"step" : "PLAN", "content" : "looking at the problem, we should solve this using BODMAS method"}
    PLAN : {"step" : "PLAN", "content" : "Yes, THE BODMAS is correct thing to be done here"}
    PLAN : {"step" : "PLAN", "content" : "first we must multiply 3 * 5 which i 15"}
    PLAN : {"step" : "PLAN", "content" : "Now the equation is 2 + 15"}
    PLAN : {"step" : "PLAN", "content" : "We must perform divide 15 / 10 = 1.5" }
    PLAN : {"step" : "PLAN", "content" : "We must perform divide 2 + 1.5 = 3.5" }
    PLAN : {"step" : "PLAN", "content" : "Finally let us perform addition" }
    PLAN : {"step" : "PLAN", "content" : "Great, we have solved and finally answer is 3.5" }
    OUTPUT : {"step" : "OUTPUT", "content" : "3.5" }
    

"""

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    response_format={"type" : "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you translate the word hello to Hindi!"},
        # Manually keep adding messages to History
        {"role" : "assistant", "content" : json.dumps({
            "step" : "START",
            "content" : "You want to a javascript code to add 'n' numbers."
        })}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
