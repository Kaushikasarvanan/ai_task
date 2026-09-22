"""System 3: AI Agent.
Uses an LLM, a private-data tool, and an agent loop.
"""

import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import client, MODEL, QUESTIONS, banner


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "students.json"
)


def get_student_data(name):
    """Tool: search the private student database."""
    with open(DATA_FILE, "r") as file:
        students = json.load(file)

    for student in students:
        if student["name"].lower() == name.lower():
            return student

    return None


def agent(question):
    """AI agent that uses the private-data tool."""

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_student_data",
                "description": "Get private student information from the college database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The student's name"
                        }
                    },
                    "required": ["name"]
                }
            }
        }
    ]

    messages = [
        {
            "role": "system",
            "content": (
                "You are a college assistant. "
                "Use the get_student_data tool when the user asks "
                "about a student's attendance, department, or internal mark."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    # Agent loop
    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content.strip()

        messages.append(message)

        for tool_call in message.tool_calls:

            if tool_call.function.name == "get_student_data":

                arguments = json.loads(tool_call.function.arguments)
                student = get_student_data(arguments["name"])

                if student is None:
                    result = "Student not found."
                else:
                    result = json.dumps(student)

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    }
                )


if __name__ == "__main__":
    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", agent(question))
        print("-" * 70)