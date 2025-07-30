import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess a state", prompt="What's a state's name?").lower()

turtle.mainloop()
# screen.exitonclick()

# TODO -
