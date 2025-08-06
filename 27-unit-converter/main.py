from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


def calculate_km():
    miles = float(usr_input.get())
    km = round(miles * 1.689, 2)
    converted_label.config(text=km)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

usr_input = Entry(width=7)
usr_input.insert(END, string="0")
usr_input.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)




window.focus_force()  # Forces window to front
window.mainloop()
