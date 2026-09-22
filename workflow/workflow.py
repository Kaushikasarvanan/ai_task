"""System 2: Rule-based workflow.
Uses fixed rules and private student data.
"""

import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import QUESTIONS, banner


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "students.json"
)


def load_students():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def find_student(name, students):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


def workflow(question):
    students = load_students()

    question_lower = question.lower()

    for student in students:
        name = student["name"].lower()

        if name in question_lower:
            if "attendance" in question_lower:
                return f"{student['name']}'s attendance is {student['attendance']}%."

            if "department" in question_lower:
                return f"{student['name']}'s department is {student['department']}."

            if "internal" in question_lower or "mark" in question_lower:
                return f"{student['name']}'s internal mark is {student['internal_mark']}."

    return "Sorry, I cannot answer this question using the available rules."


if __name__ == "__main__":
    banner("SYSTEM 2: RULE-BASED WORKFLOW")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)