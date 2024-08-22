from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()

print("Bạn đã hoàn thành bài test")
print(f"Điểm tổng kết của bạn là: {quiz.score}/{quiz.question_number}")

