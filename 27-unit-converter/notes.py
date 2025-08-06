# import tkinter # If using one or 2 classes
from tkinter import *  # If you're using lots of classes, so you have to type tkinter.*

window = Tk()
window.title("This is a GUI")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()
my_label["text"] = "New text1"
my_label.config(text="New text2")


# Button
def button_clicked():
    # my_label.config(text=usr_input.get())
    my_label.config(text="button pushed")
    # or
    # new_text = usr_input.get()
    # my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
# usr_input = Entry(width=10)
# usr_input.pack()
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))  # The 1.0 refers to the first line (1) and the char at index 0 for getting text
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to the checked state, 0 is off, 1 is on.
checked_state = IntVar()  # is a class that needs to be init got the get method
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

window.focus_force()  # Forces window to front
window.mainloop()

# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
#
#
# print(add(1, 2, 3, 4))

# def calculate(n, **kwargs):
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)

# Create a class with optional kwargs
# class Car:
#     def __init__(self, **kwargs):
#         # self.make = kwargs["make"]
#         # self.model = kwargs["model"]
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#
#
# my_car = Car(make="Honda")
# print(my_car.make)
# print(my_car.model)
