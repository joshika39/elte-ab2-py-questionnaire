import os
import re
from typing import List

class Question:
    def __init__(self, number, question: str, points: int, answer: str):
        self.question = question.strip()
        self.points = points
        self.answer = answer.strip()
        self.number = number

    def __repr__(self):
        return f"Question(points={self.points}, question={self.question[:30]}...)"

    def __str__(self):
        return f"{self.number}.\t{self.question}"

def parse_question_pool(file_content: str) -> List[Question]:
    question_pattern = re.compile(r"## (\d+)\. (.*?)\((\d+) pont\)\n(.*?)(?=\n## |\Z)", re.DOTALL)

    questions = []
    for match in question_pattern.finditer(file_content):
        question_number = int(match.group(1))
        question_text = match.group(2)
        points = int(match.group(3))
        answer = match.group(4)
        questions.append(Question(question_number, question_text, points, answer))
    
    return questions

def filter_questions_by_difficulty(questions: List[Question], points: int) -> List[Question]:
    return [q for q in questions if q.points == points]

def print_questions(questions: List[Question]):
    ordered_questions = sorted(questions, key=lambda q: q.number)
    for q in ordered_questions:
        print(q)

if __name__ == "__main__":
    with open("./questions/kerdesek.md", "r", encoding="utf-8") as file:
        file_content = file.read()

    questions = parse_question_pool(file_content)

    while True:
        num = input("Please enter the difficulty level: ")
        try:
            easy_questions = filter_questions_by_difficulty(questions, int(num))
            os.system("clear")
            print_questions(easy_questions)
        except ValueError:
            if num == "q":
                exit()

