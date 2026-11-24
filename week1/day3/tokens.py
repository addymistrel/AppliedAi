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
prompt1 = "Hi"
prompt2 = "Explain time travel in detail"
prompt3 = "Write 1000 words on machine learning"
prompt = "Suggest a name for my food company. You Only tell me one liner response"


messages: list[ChatCompletionMessageParam] = []

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message: ChatCompletionMessageParam = {
        "role": "user",
        "content": prompt
    }

    messages.append(message)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=5000,
    )
    usage = response.usage
    prompt_tokens = usage.prompt_tokens if usage is not None else 0
    completion_tokens = usage.completion_tokens if usage is not None else 0
    finish_reason = response.choices[0].finish_reason
    print(f"Prompt: {prompt} --> your_tokens: {prompt_tokens} -->  completion_tokens: {completion_tokens} --> total_tokens: {prompt_tokens + completion_tokens} --> finish_reason = {finish_reason}")