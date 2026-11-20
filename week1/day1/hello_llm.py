import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ API KEY NOT FOUND")

client = Groq(api_key=groq_api_key)

model = "openai/gpt-oss-20b"
role = "user"
prompt = "Do you know addymistrel"

response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
)
print(response.choices[0].message.content)