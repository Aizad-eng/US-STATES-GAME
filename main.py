import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
tim = turtle.Turtle()

turtle.shape(image)
data = pd.read_csv("50_states.csv")
states_and_coorinates ={}
for index, row in data.iterrows():
    state = row['state']
    x = row['x']
    y = row['y']
    states_and_coorinates[state] = (x, y)
states_already_learnt = []
states_to_learn = []
states = [key for key, value in states_and_coorinates.items()]
user_score=0
tim.hideturtle()
chances=3
print(f"You have {chances} Chances available")
while chances>0:
    user_choice = screen.textinput(f"{user_score}/{len(data)} ", prompt="Which state? ").title()
    if user_choice.lower() == "exit":
        print("Exiting the Game!")
        chances = 0
    elif user_choice in states and user_choice not in states_already_learnt:
        user_score+=1
        states_already_learnt.append(user_choice)
        tim.penup()
        tim.goto(states_and_coorinates[user_choice])
        tim.write(user_choice, move=False, align='left', font=('Arial', 8, 'normal'))
        tim.pendown()
        found = True

    elif user_choice not in states:
        chances -= 1
        if chances>=1:
            print(f"{user_choice} is not a valid US state. You have {chances} Chance(s) left")
        else:
            print("You have no chances left, Game Over")
            print("Please open the csv file States to learn.csv to learn about the remaining states")

for state in states:
    if state not in states_already_learnt:
        states_to_learn.append(state)

data = {"States To Learn": states_to_learn}
df = pd.DataFrame(data)
df.to_csv("States to learn.csv")
screen.exitonclick()
