class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list

    def still_has_qs(self):
        pass # needs to check if there more questions and return bool

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        input(f"Q{self.question_num}: {question.text} (True/False)?: ").lower()
