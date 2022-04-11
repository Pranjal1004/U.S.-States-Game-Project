import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_answers = data["state"].tolist()
correct_guess = []


def write_state_on_map(state_name):
    state_x_cor = data[data.state == state_name]["x"].tolist()
    new_x = int(state_x_cor[0])
    state_y_cor = data[data.state == state_name]["y"].tolist()
    new_y = int(state_y_cor[0])

    turtle2 = turtle.Turtle()
    turtle2.hideturtle()
    turtle2.penup()
    turtle2.goto(new_x, new_y)
    turtle2.write(state_name, align="center", font=("Arial", 8, "normal"))


game_is_on = True
while game_is_on:
    current_score = len(correct_guess)
    answer_state = screen.textinput(title=f" {current_score}/ 50 Correct State",
                                    prompt="What's another state name?").title()
    print(answer_state)
    if current_score >= 50:
        game_is_on = False
    if answer_state == "Exit":
        break
    for correct_state in correct_answers:
        if answer_state == correct_state:
            correct_guess.append(correct_state)
            write_state_on_map(correct_state)


# states_unanswered = []
# for state in correct_answers:
#     if state not in correct_guess:
#         states_unanswered.append(state)
states_unanswered = [state for state in correct_answers if state not in correct_guess]
states_left_dict = {"States to Learn": states_unanswered}
states_left = pandas.DataFrame.from_dict(states_left_dict)
states_left.to_csv("states_to_learn.csv")


# screen.exitonclick()
