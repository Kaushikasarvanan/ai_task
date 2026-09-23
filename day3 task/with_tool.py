from tool import calculate_total

print("TOOL-ENABLED LLM RUN")
print()

question = "What is the total cost of 3 apples at ₹20 each and 2 notebooks at ₹50 each?"

print("Question:", question)
print()

print("LLM decision: A calculation tool is needed.")

prices = [20, 20, 20, 50, 50]

print("Tool call: calculate_total([20, 20, 20, 50, 50])")

result = calculate_total(prices)

print("Tool result:", result)
print()

print("Final answer:", result)