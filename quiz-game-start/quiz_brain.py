class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {current_question.text} (Đúng/Sai): ")
        self.check_answer(guess, current_question.answer)

    def check_answer(self, guess, correct_answer):
        if guess.lower() == correct_answer.lower():
            print("Câu trả lời chính xác!")
            self.score += 1
        else:
            print("Sai rồi")
        print(f"Câu trả lời đúng là: {correct_answer}.")
        print(f"Điểm số của bạn là: {self.score}/{self.question_number}")
        print("\n")

