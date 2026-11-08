from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in few words"
)


print(response.text)

