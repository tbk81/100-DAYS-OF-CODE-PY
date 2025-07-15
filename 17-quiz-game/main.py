from question_model import Question
from data import question_data


question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

print(question_bank[0].)
