import os
from openai import OpenAI
import json

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
print(client.api_key)

with open('test_question_content.json', 'r') as file:
    question_content_str = json.load(file)

question_content = question_content_str['test_question']

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": "You are a sports fan."
        },
        {
            "role": "user",
            "content": question_content
        }
    ]
)

print(completion.choices[0].message)