import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess a state", prompt="What's a state's name?").capitalize()
# print(data.state)
# if "Alaska" in data.state.values:
#     print("yes")
print(answer_state)
show_state = turtle.Turtle()
print(screen.screensize())
if answer_state in data.state.values:
    print("Correct")
    guess = data[data.state == answer_state]
    print(guess.x)
    print(type(guess.x))
    x = guess.x.astype(int)
    print(x)
    print(guess.y)
    state_coords = (x, guess.y)
    # print(type(state_coords))
    print(state_coords)
    # show_state.goto(x=guess.x, y=guess.y)

# turtle.mainloop()
screen.exitonclick()







# TODO.1 - Convert the guess to title case - DONE
# TODO.2 - Check if the guess is amoung the states - D
# TODO.3 - Write the correct guesses on the map
# TODO.4 - Use a loop to let the user keep guessing
# TODO.5 - Record the correct guesses in a list
# TODO.6 - Keep track of the score

