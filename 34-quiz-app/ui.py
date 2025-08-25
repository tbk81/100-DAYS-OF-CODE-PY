from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz hole")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some text goes here",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 16))
        self.score_label.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,
                                  highlightthickness=0,
                                  highlightbackground=THEME_COLOR,
                                  command=self.is_true
                                  )
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,
                                   highlightthickness=0,
                                   highlightbackground=THEME_COLOR,
                                   command=self.is_false
                                   )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.focus_force()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def is_true(self):
        self.feedback(self.quiz.check_answer("true"))

    def is_false(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)