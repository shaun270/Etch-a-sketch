#ATTENTION USERS!!
# 'Up' key to move forwards, 'Down' key to move backwards, 'a' key to move counter clockwise
#'d' key to move clockwise, 'c' key to clear your drawing

import turtle
from turtle import Turtle,Screen

tim=Turtle()

def forwards():
    tim.forward(5)

def backwards():
    tim.back(5)

def counter_clock():
    tim.left(5)

def clock():
    tim.right(5)

def clear():
    tim.clear()
    tim.reset()

turtle.listen()
turtle.onkey(forwards,"Up")
turtle.onkey(backwards,"Down")
turtle.onkey(counter_clock,"a")
turtle.onkey(clock,"d")
turtle.onkey(clear,"c")



screen=Screen()
screen.exitonclick()

