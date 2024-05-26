import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Names")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)
guessed_states = []

while len(guessed_states) < 50:

    state_input = screen.textinput(f"{len(guessed_states)}/50 States Correct","Write the name of state").title()
    # state_input = input("Write the name of state")
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    state_name = data["state"]
    if state_input in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        guessed_states.append(state_input)
        state_data = data[data.state == state_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    if(state_input == "Quit" or state_input == "Exit"):
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        # print(states_to_learn)
        data_learn = pandas.DataFrame(states_to_learn)
        data_learn.to_csv("states_to_learn.csv")
        break

screen.exitonclick()