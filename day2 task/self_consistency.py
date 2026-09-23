from groq import Groq
import os
from dotenv import load_dotenv
from collections import Counter

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

question = """
I have ₹5,000.
Three activities cost ₹1,200, ₹800, and ₹1,500.
How much money will remain?

Give only the final numerical answer.
"""

answers = []

print("SELF-CONSISTENCY")
print("----------------")
print("Running the same question 5 times...\n")

for i in range(5):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content.strip()

    answers.append(answer)

    print(f"Run {i + 1}: {answer}")

# Find the most common answer
counts = Counter(answers)
majority_answer = counts.most_common(1)[0][0]

print("\n----------------")
print("MAJORITY ANSWER:")
print(majority_answer)

print("\nExpected correct answer: ₹1,500")