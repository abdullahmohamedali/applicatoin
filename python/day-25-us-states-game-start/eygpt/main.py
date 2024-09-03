import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "3328.gif"

# data = pandas.read_csv("eypt_stats.csv")
# # all_states = data.state.to_list()
# # gussed_state = []
screen.addshape(image)
turtle.shape(image)


def get_mouse_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_coor)
turtle.mainloop()

# while len(gussed_state) < 50:
#     answer_state = screen.textinput(title=f"{len(gussed_state)}/50", prompt="whrite the state")
#     answer_state = answer_state.title()
#     if answer_state in all_states:
#         gussed_state.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)
