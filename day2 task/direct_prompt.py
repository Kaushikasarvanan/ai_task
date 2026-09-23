from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

question = """
I have ₹5,000.
Three activities cost ₹1,200, ₹800, and ₹1,500.
How much money will remain?
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print("DIRECT PROMPTING")
print("----------------")
print("Question:", question)
print("Answer:", response.choices[0].message.content)