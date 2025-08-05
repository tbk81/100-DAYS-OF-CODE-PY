import tkinter  # If using one or 2 classes
from tkinter import *  # If you're using lots of classes so you have to type tkinter.*

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
    my_label.config(text=usr_input.get())
    # or
    # new_text = usr_input.get()
    # my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
usr_input = Entry(width=10)
usr_input.pack()




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
