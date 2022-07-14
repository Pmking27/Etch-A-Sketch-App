#Make an Etch-A-Sketch App
from turtle import Turtle,Screen

timmy=Turtle()
screen = Screen()
timmy.speed(1)

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_anticlockwise():
    timmy.left(10)

def move_clockwise():
    timmy.right(10)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown() 

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_anticlockwise,"a")
screen.onkey(move_clockwise,"d")
screen.onkey(clear_screen,"c")

screen.exitonclick()    