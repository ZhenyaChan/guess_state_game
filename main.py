import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        x = data[data.state == answer_state].x.iloc[0]
        y = data[data.state == answer_state].y.iloc[0]
        new_state.goto(x, y)
        new_state.write(answer_state)


# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# grey_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_count, cinnamon_count, black_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
