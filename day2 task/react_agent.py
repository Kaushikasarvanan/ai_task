from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# TOOL 1: Calculate remaining money
def calculate_remaining_money(total, expenses):
    return total - sum(expenses)


# TOOL 2: Get weather information
def get_weather(city):
    weather_data = {
        "Ooty": "18°C, cloudy"
    }

    return weather_data.get(city, "Weather information not available")


# Tool definitions for the model
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_remaining_money",
            "description": "Calculate the money remaining after expenses.",
            "parameters": {
                "type": "object",
                "properties": {
                    "total": {
                        "type": "number",
                        "description": "Total amount of money"
                    },
                    "expenses": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        },
                        "description": "List of expenses"
                    }
                },
                "required": ["total", "expenses"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather information for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]


question = """
I am planning a trip to Ooty.

I have ₹5,000.
My activities cost ₹1,200, ₹800, and ₹1,500.

I also want to know the weather in Ooty.

Find:
1. How much money will remain?
2. What is the weather in Ooty?
"""


messages = [
    {
        "role": "user",
        "content": question
    }
]


print("REACT AGENT")
print("-----------")
print("Question:")
print(question)


# First model call
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    temperature=0
)

message = response.choices[0].message


# Check whether the model requested a tool
if message.tool_calls:

    messages.append(message)

    for tool_call in message.tool_calls:

        function_name = tool_call.function.name
        arguments = eval(tool_call.function.arguments)

        print("\nAction:", function_name)
        print("Arguments:", arguments)

        if function_name == "calculate_remaining_money":

            result = calculate_remaining_money(
                arguments["total"],
                arguments["expenses"]
            )

        elif function_name == "get_weather":

            result = get_weather(
                arguments["city"]
            )

        else:
            result = "Unknown tool"

        print("Observation:", result)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
        )


    # Second model call after observing tool results
    final_response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    print("\nFinal Answer:")
    print(final_response.choices[0].message.content)

else:

    print("\nFinal Answer:")
    print(message.content)