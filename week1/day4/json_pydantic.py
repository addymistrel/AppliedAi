import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from groq.types.chat import ChatCompletionMessageParam
from typing import Literal, TypedDict

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ API KEY NOT FOUND")

client = Groq(api_key=groq_api_key)

model = "openai/gpt-oss-20b"
role = "user"

# structure it
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()


class ResponseFormat(TypedDict):
    type: Literal["json_object"]

response_format: ResponseFormat = {
    "type": "json_object"
}

system_prompt = f"""
Extract the personal information from the customer ticket.

Return the response in valid JSON format only.
Follow this JSON schema strictly:

{schema}
"""

system_message: ChatCompletionMessageParam = {
    "role": "system",
    "content": system_prompt
}

text = "Hello My name is Aditya. I have an iphone which is not working at all. My address is delhi. My email is addymistrel@gmail.com. My contact number is 1234."
prompt = f'''
This is a customer ticket. Please extract the personal information from this.
{text}
'''

user_message: ChatCompletionMessageParam = {
    "role": "user", 
    "content": prompt
}

messages: list[ChatCompletionMessageParam] = [system_message, user_message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)
ans = response.choices[0].message.content

import json
raw_json: str | None = ans
data_file = json.loads(raw_json if raw_json else "")
ticket = Ticket(**data_file)
 
print(ticket.name)
print(ticket.email)
print(ticket.issue)
