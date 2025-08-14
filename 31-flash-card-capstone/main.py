from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")

df = pandas.read_csv("data/common_ports.csv")
to_learn = df.to_dict(orient="records")

current_card = {}  # Empty dict to be able to access from other functions
print(to_learn)

# ---------------------------- Next port button ------------------------------- #

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Stops timer  after clicking button
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="Port Number", fill="black")
    canvas.itemconfig(port, text=current_card["port_num"], fill="black")
    canvas.itemconfig(card_bg, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)  # New timer after the card has been flipped


def flip_card():
    canvas.itemconfig(title, text="Service", fill="white")
    canvas.itemconfig(port, text=current_card["service"], fill="white")
    canvas.itemconfig(card_bg, image=back_card_img)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Hole")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=850, height=576, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(425, 288, image=front_card_img)
canvas.grid(column=0, row =0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,
                      highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0,
                        highlightbackground=BACKGROUND_COLOR, command=next_card)
correct_button.grid(column=1, row=1)

# Canvas text
title = canvas.create_text(400, 150, text="", fill="black", font=FONT)
port = canvas.create_text(400, 263, text="", fill="black", font=FONT)


next_card()
window.focus_force()
window.mainloop()
