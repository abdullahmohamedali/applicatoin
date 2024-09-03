import tkinter
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    Canvas.itemconfig(card_title, text="french", fill="black")
    Canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    Canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)
def flip_card():
    Canvas.itemconfig(card_title, text="English", fill="white")
    Canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    Canvas.itemconfig(card_background, image=card_back_img)

window = tkinter.Tk()

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("flashy")

flip_timer = window.after(3000, flip_card)


Canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png",)
card_back_img = PhotoImage(file="images/card_back.png")
card_background = Canvas.create_image(400, 263, image=card_front_img)

card_title = Canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
card_word = Canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))

Canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
Canvas.grid(row=0, column=0, columnspan=2)

true_button_img = PhotoImage(file="images/right.png")
true_button = Button(image=true_button_img, highlightthickness=0, command=next_card)
true_button.grid(row=1,column=1)

false_button_img = PhotoImage(file="images/wrong.png")
false_button = Button(image=false_button_img, highlightthickness=0, command=next_card)
false_button.grid(row=1, column=0)

next_card()
window.mainloop()