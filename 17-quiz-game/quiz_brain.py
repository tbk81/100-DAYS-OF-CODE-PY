from distutils.command.check import check


class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list

    def still_has_qs(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        usr_ans = input(f"Q.{self.question_num}: {question.text} (True/False)?: ").lower()
        self.check_answer(usr_ans, question.answer)

    def check_answer(self, usr_ans, correct_ans):
        if usr_ans == correct_ans.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The correct answer was {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_num}")
        print("\n")
