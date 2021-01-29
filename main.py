from turtle import Turtle, Screen
import random

colors = ["red","yellow","blue","black","green"]
pos_start = [-140, -70, 0, 70, 140]
all_turtles = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Your bet", prompt="Which color: ")
is_race_on = False

for turtle_idx in range(0,5):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_idx])
    tim.penup()
    tim.goto(x=-230, y=pos_start[turtle_idx])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! {winning_turtle}")
            else:
                print(f"Sorry try again! The winner is {winning_turtle}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()