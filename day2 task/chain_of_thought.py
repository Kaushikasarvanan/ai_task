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

Explain the calculation step by step.
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

print("CHAIN-OF-THOUGHT")
print("----------------")
print("Question:", question)
print("Answer:")
print(response.choices[0].message.content)