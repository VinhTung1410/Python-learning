import random
from turtle import Turtle, Screen

screen =Screen()
cnt = 0
screen.bgcolor("grey")
screen.setup(500,400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_position = [-70, -40, -10, 20, 50, 80]
color = ["orange", "blue", "yellow", "red", "green", "black"]
all_turtles = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(x=-230, y=y_position[i])
    all_turtles.append(tim)

while cnt < 6:
    for i in all_turtles:
        if i.xcor() > 230:
            cnt += 1
            win = i.pencolor()
            all_turtles.remove(i)

            if cnt == 1:
                if bet == win:
                    print("You win!!! Congratulation")
                else:
                    print("You lose! Nice try")
            if bet == win:
                print(f"Your turtle {win} is rank {cnt}")
            else:
                print(f"Turtle {win} is rank {cnt}")



        rand_distance = random.randint(1,10)
        i.forward(rand_distance)

screen.exitonclick()




