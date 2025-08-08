from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# noinspection DuplicatedCode
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# pw = []
# for n in range(2, 10):
#     pw.append(random.choice(letters))

pw = [random.choice(letters) for n in range(2, 10)]
# pw.append([random.choice(numbers) for n in range(2, 4)])
# pw = [random.choice(symbols) for n in range(2, 4)]

random.shuffle(pw)
pw = "".join(pw)

print(pw)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_un_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill all the fields")
    else:
        accept = messagebox.askokcancel(website, f"Email: {email}\nPassword{password}\n"
                                                 f"Do you want to save this password?")
        if accept:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=20, bg="white")

canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", fg="black", bg="white")
website_label.grid(column=0, row=1, sticky="E")

email_un_label = Label(text="Email/Username:", fg="black", bg="white")
email_un_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3, sticky="E")

# Entries
website_entry = Entry(width=34, bg="white", highlightthickness=0.1)
website_entry.grid(column=1, row=1, rowspan=1, pady=2, padx=2)
website_entry.focus()

email_un_entry = Entry(width=34, bg="white", highlightthickness=0.1)
email_un_entry.grid(column=1, row=2, rowspan=1, pady=2, padx=2)
email_un_entry.insert(0, "tbk@gmail.com")

password_entry = Entry(width=17, bg="white", highlightthickness=0.1)
password_entry.grid(column=1, row=3, pady=2, padx=(5, 0), sticky="W")

# Buttons
generate_pw_button = Button(text="Generate Password", highlightbackground="white")
generate_pw_button.grid(column=1, row=3,sticky="E")

add_button = Button(text="Add", width=32, highlightbackground="white", command=save)
add_button.grid(column=1, row=4, rowspan=1)


window.focus_force()
window.mainloop()
