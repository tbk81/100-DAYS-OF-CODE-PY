from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from comp_sci_data import comp_question_data

# This is using the provided question data
question_bank = []
for q in comp_question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))

# for q in comp_question_data:
#     question_bank.append(Question(q["text"], q["answer"]))

# for q in comp_question_data:
#     print(q["question"])
#     print(q["correct_answer"])

# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_qs():
    quiz.next_question()

print(f"You've completed the quiz!\nYou got {quiz.score}/{quiz.question_num} correct.")
