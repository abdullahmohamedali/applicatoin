import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
gussed_state = []
screen.addshape(image)
turtle.shape(image)
while len(gussed_state) < 50:
    answer_state = screen.textinput(title=f"{len(gussed_state)}/50", prompt="whrite the state")
    answer_state = answer_state.title()
    if answer_state in all_states:
        gussed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

