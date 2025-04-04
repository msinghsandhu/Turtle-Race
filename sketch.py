from turtle import Turtle,Screen

timmy_the_turtle = Turtle()

def move_forward():
  timmy_the_turtle.forward(10)  
def move_backward():
  timmy_the_turtle.backward(10)
def move_counter_clockwise():
  timmy_the_turtle.left(10)
def move_clockwise():
  timmy_the_turtle.right(10)
def clear():
  timmy_the_turtle.reset()
  timmy_the_turtle.clear()

screen = Screen()
screen.listen()
screen.onkey(key = "w",fun=move_forward)
screen.onkey(key = "s",fun=move_backward)
screen.onkey(key = "a",fun=move_counter_clockwise)
screen.onkey(key = "d",fun=move_clockwise)
screen.onkey(key = "c",fun=clear)
screen.exitonclick()
