from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=10, bg=THEME_COLOR)
        self.quiz = quiz_brain

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150 ,125 ,text="somthing",width=280, fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img,highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_button_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=false_button_img,highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=1)

        self.next_questoin()
        self.window.mainloop()

    def next_questoin(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_questoin)






