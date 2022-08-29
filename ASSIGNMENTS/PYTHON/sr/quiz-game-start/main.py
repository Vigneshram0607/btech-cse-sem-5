from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    qn_text = question["question"]
    qn_ans = question["correct_answer"]
    new_qn = Question(qn_text, qn_ans)
    question_bank.append(new_qn)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've Succesfully completed Our Quiz!!!!")
print(f"And Your Score : {quiz.score}/{quiz.question_number}")
