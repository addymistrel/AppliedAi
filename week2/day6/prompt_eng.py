import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from groq.types.chat import ChatCompletionMessageParam

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ API KEY NOT FOUND")

client = Groq(api_key=groq_api_key)
model = "openai/gpt-oss-20b"

def llm_ans(prompt):
    message: ChatCompletionMessageParam = {
        "role": "user",
        "content": prompt
    }
    messages: list[ChatCompletionMessageParam] = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans = response.choices[0].message.content
    return ans

bad_prompt = """
#ROLE:
You are a support assistant at a mobile/laptop company.
#TASK:
You have to classify the issue in a category
#CONSTRAINT:
You have to classify the issue in one of the three categories namely Billing, Technical, Return
#OUTPUT FORMAT
Your answer should be in one word only. The one word should be one of teh categories given in constraint
#Example
For instance if a user complain says he wants a refund the category is refund.
#FALLBACK
If the issue is unrelated to any of the categories mentioned in any of the constraints, then the answer should be 'Other'
This is a user complaint
My laptop stopped working
classify this
"""

print(llm_ans(bad_prompt))