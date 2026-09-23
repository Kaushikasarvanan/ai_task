print("NO-TOOL LLM RUN")
print()

questions = [
    "What is Python?",
    "What is an AI agent?",
    "What is the total cost of 3 apples at ₹20 each and 2 notebooks at ₹50 each?"
]

answers = [
    "Python is a high-level programming language.",
    "An AI agent is a system that can use an LLM and tools to perform tasks.",
    "The total cost is ₹160."
]

for question, answer in zip(questions, answers):
    print("Question:", question)
    print("Answer:", answer)
    print()