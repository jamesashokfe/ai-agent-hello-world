"""
A simple Hello World AI agent that sends a user query to OpenRouter API and displays the response.
"""

import os
from openai import OpenAI, api_key
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("API key not found in environment variables")

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Prompt
user_query = input("User: ")

# Send query and get response
response = client.chat.completions.create(
    model="openai/gpt-oss-20b:free",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_query}
    ]
)

# Show response
ai_reply = response.choices[0].message.content
print("AI agent: ", ai_reply)
