from groq import Groq

client = Groq()

MODEL = "openai/gpt-oss-20b"

QUESTIONS = [
    "What is Rahul's attendance?",
    "What is Priya's department?"
]


def banner(title):
    print("=" * 70)
    print(title)
    print("=" * 70)