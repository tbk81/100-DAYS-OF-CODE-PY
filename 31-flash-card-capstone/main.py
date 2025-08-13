from tkinter import *
import pandas



BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Hole")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=850, height=576, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(425, 288, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)

# Canvas text
port_num = canvas.create_text(400, 150, text="Port Number", font=FONT)
num = canvas.create_text(400, 263, text="53", font=FONT)


window.focus_force()
window.mainloop()
