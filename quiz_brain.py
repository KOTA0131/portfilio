# TODO:asking the questions
# TODO:checking if the answer was correct
# TODO:checking if we're the end of the quiz
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.q_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Good")
            self.new_score()
        else:
            print("Bad")
        self.show_score()
    def new_score(self):
        self.score += 1

    def show_score(self):
        print(f"Your current score is: {self.score}/{self.question_number}")
