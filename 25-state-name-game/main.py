import turtle as t
import pandas
from map_manager import MapManager

# Screen Set up
screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
remaining_states = []
map_manager = MapManager()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's a state's name?").title()
    if answer_state == "Exit":
        break

    if answer_state in data.state.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        guess = data[data.state == answer_state]
        state_coords = (guess.x.item(), guess.y.item())
        map_manager.show_state(answer_state, state_coords)







# TODO.1 - Convert the guess to title case - DONE
# TODO.2 - Check if the guess is among the states - DONE
# TODO.3 - Write the correct guesses on the map - DONE
# TODO.4 - Use a loop to let the user keep guessing - DONE
# TODO.5 - Record the correct guesses in a list - DONE
# TODO.6 - Keep track of the score - DONE

