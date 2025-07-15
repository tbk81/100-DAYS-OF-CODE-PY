from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
quiz.next_question()
