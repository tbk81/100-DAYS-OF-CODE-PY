from tkinter import *

from sqlalchemy.ext.automap import generate_relationship

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=20, bg="white")

canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", fg="black", bg="white")
website_label.grid(column=0, row=1, sticky="E")

email_un_label = Label(text="Email/Username:", fg="black", bg="white")
email_un_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3, sticky="E")

website_entry = Entry(width=34, bg="white", highlightthickness=0.1)
website_entry.grid(column=1, row=1, rowspan=1, pady=2, padx=2)

email_un_entry = Entry(width=34, bg="white", highlightthickness=0.1)
email_un_entry.grid(column=1, row=2, rowspan=1, pady=2, padx=2)

password_entry = Entry(width=17, bg="white", highlightthickness=0.1)
password_entry.grid(column=1, row=3, pady=2, padx=(5, 0), sticky="W")

generate_pw_button = Button(text="Generate Password", highlightbackground="white")
generate_pw_button.grid(column=1, row=3,sticky="E")

add_button = Button(text="Add", width=32, highlightbackground="white")
add_button.grid(column=1, row=4, rowspan=1)


window.focus_force()
window.mainloop()
