# 	1. Modify the data.py file (don't change the main.py)
# 	2. Make a get() request to fetch 10 True or False questions.
# 	3. Parse the JSON response and replace  the value of question_data (don't change the variable name)
# 	Hint: create a python dictionary for the amount and type parameters.

import requests

response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
