import re
from typing import List

class Question:
    def __init__(self, question: str, points: int, answer: str):
        self.question = question.strip()
        self.points = points
        self.answer = answer.strip()

    def __repr__(self):
        return f"Question(points={self.points}, question={self.question[:30]}...)"

def parse_question_pool(file_content: str) -> List[Question]:
    question_pattern = re.compile(r"## (\d+)\. (.*?)\((\d+) pont\)\n(.*?)(?=\n## |\Z)", re.DOTALL)

    questions = []
    for match in question_pattern.finditer(file_content):
        question_number = int(match.group(1))
        question_text = match.group(2)
        points = int(match.group(3))
        answer = match.group(4)
        questions.append(Question(question_text, points, answer))
    
    return questions

def filter_questions_by_difficulty(questions: List[Question], points: int) -> List[Question]:
    return [q for q in questions if q.points == points]

if __name__ == "__main__":
    with open("question_pool.txt", "r", encoding="utf-8") as file:
        file_content = file.read()

    questions = parse_question_pool(file_content)

    easy_questions = filter_questions_by_difficulty(questions, 1)
    
    print(f"Total Questions: {len(questions)}")
    print(f"Easy Questions: {len(easy_questions)}")
    for q in easy_questions[:5]:  # Display the first 5 easy questions
        print(q)
