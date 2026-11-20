import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from groq.types.chat import ChatCompletionMessageParam
from typing import List

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ API KEY NOT FOUND")

client = Groq(api_key=groq_api_key)

model = "openai/gpt-oss-20b"
role = "user"
prompt = "Suggest a name for my food company. You Only tell me one liner response"

message_system: ChatCompletionMessageParam = {
    "role": "system",
    "content": "You are a brand manager who suggest name for my food brand. "
}

message: ChatCompletionMessageParam = {
    "role": "user",
    "content": prompt
}

messages: list[ChatCompletionMessageParam] = [message_system, message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2
)
print(response.choices[0].message.content)