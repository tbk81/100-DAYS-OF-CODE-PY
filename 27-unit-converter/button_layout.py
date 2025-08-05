from tkinter import *  # If you're using lots of classes so you have to type tkinter.*

def button_clicked():
    new_text = usr_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("This is a GUI")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.config(text="New text2")
# my_label.pack()
# my_label.place(x=100, y=50)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry
usr_input = Entry(width=10)
entry = Entry(width=30)
# usr_input.pack()
usr_input.grid(column=2, row=1)


window.focus_force()  # Forces window to front
window.mainloop()

