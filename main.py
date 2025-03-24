# # # # from turtle import Turtle, Screen
# # # # import random


# # # # is_race_on = False
# # # # rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue"]

# # # # screen = Screen()
# # # # screen.setup(width=500,height=400)
# # # # user_bet = screen.textinput(title="Make your bet",prompt="which turtle will win the race? Enter a color:")
# # # # print(user_bet)
# # # # y = -60

# # # # all_turtles = []
# # # # for i in range(5):
# # # #   new_turtle = Turtle('turtle')
# # # #   new_turtle.color(rainbow_colors[i])
# # # #   new_turtle.penup()
# # # #   new_turtle.goto(x=-230,y=y)
# # # #   y +=30
# # # #   all_turtles.append(new_turtle)

# # # # if user_bet:
# # # #   is_race_on = True

# # # # while is_race_on:

# # # #   for turtle in all_turtles:
# # # #     if turtle.xcor() >230:
# # # #       is_race_on = False
      
# # # #       winning_color = turtle.pencolor()
# # # #       if winning_color.lower() == user_bet.lower():
# # # #         print(f'You have won! Then {winning_color} turtle is the winner')
# # # #       else:
# # # #         print(f'You have lost! Then {winning_color} turtle is the winner')
# # # #     random_distance = random.randint(1,10)
# # # #     turtle.forward(random_distance)

# # # # screen.exitonclick()


# # # from turtle import Turtle, Screen
# # # import random

# # # # Screen Setup
# # # screen = Screen()
# # # screen.title("Turtle Race - Aesthetic UI")
# # # screen.setup(width=600, height=400)
# # # screen.bgcolor("lightblue")

# # # # Draw Finish Line
# # # finish_line = Turtle()
# # # finish_line.hideturtle()
# # # finish_line.penup()
# # # finish_line.goto(230, -100)
# # # finish_line.pendown()
# # # finish_line.pensize(3)
# # # finish_line.color("black")

# # # for _ in range(10):
# # #     finish_line.forward(10)
# # #     finish_line.penup()
# # #     finish_line.forward(10)
# # #     finish_line.pendown()

# # # # Turtle Colors and Starting Positions
# # # rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
# # # y_positions = [-60, -30, 0, 30, 60]

# # # # User Bet
# # # user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
# # # all_turtles = []

# # # # Create Turtles
# # # for i in range(5):
# # #     new_turtle = Turtle('turtle')
# # #     new_turtle.color(rainbow_colors[i])
# # #     new_turtle.penup()
# # #     new_turtle.goto(x=-230, y=y_positions[i])
# # #     all_turtles.append(new_turtle)

# # # # Start Race if Bet is Placed
# # # if user_bet:
# # #     is_race_on = True
# # # else:
# # #     is_race_on = False

# # # while is_race_on:
# # #     for turtle in all_turtles:
# # #         if turtle.xcor() > 230:
# # #             is_race_on = False
# # #             winning_color = turtle.pencolor()
            
# # #             # Display Result
# # #             result_turtle = Turtle()
# # #             result_turtle.hideturtle()
# # #             result_turtle.penup()
# # #             result_turtle.goto(-100, 0)
# # #             result_turtle.color("black")
# # #             result_turtle.write(
# # #                 f"You {'won' if winning_color.lower() == user_bet.lower() else 'lost'}! "
# # #                 f"The {winning_color} turtle is the winner!",
# # #                 align="center",
# # #                 font=("Arial", 14, "bold")
# # #             )

# # #         random_distance = random.randint(1, 10)
# # #         turtle.forward(random_distance)

# # # screen.exitonclick()


# # from turtle import Turtle, Screen
# # import random

# # # Screen Setup
# # screen = Screen()
# # screen.title("Turtle Race - Aesthetic UI")
# # screen.setup(width=600, height=400)
# # screen.bgcolor("#DDEEFF")  # Soft gradient-like blue

# # # Draw Track Lanes
# # track_lines = Turtle()
# # track_lines.hideturtle()
# # track_lines.penup()
# # track_lines.color("gray")

# # for y in [-75, -45, -15, 15, 45, 75]:  # Lane dividers
# #     track_lines.goto(-250, y)
# #     track_lines.pendown()
# #     track_lines.forward(500)
# #     track_lines.penup()

# # # Draw Finish Line
# # finish_line = Turtle()
# # finish_line.hideturtle()
# # finish_line.penup()
# # finish_line.goto(230, -90)
# # finish_line.pendown()
# # finish_line.pensize(3)
# # finish_line.color("black")

# # for _ in range(10):
# #     finish_line.forward(10)
# #     finish_line.penup()
# #     finish_line.forward(10)
# #     finish_line.pendown()

# # # Turtle Colors and Positions
# # rainbow_colors = ["red", "orange", "yellow", "green", "blue"]
# # y_positions = [-60, -30, 0, 30, 60]

# # # User Bet
# # user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
# # all_turtles = []

# # # Create Turtles
# # for i in range(5):
# #     new_turtle = Turtle('turtle')
# #     new_turtle.color(rainbow_colors[i])
# #     new_turtle.shapesize(1.3)  # Make turtles slightly bigger
# #     new_turtle.penup()
# #     new_turtle.goto(x=-230, y=y_positions[i])
# #     all_turtles.append(new_turtle)

# # # Start Race if Bet is Placed
# # is_race_on = bool(user_bet)

# # while is_race_on:
# #     for turtle in all_turtles:
# #         if turtle.xcor() > 230:
# #             is_race_on = False
# #             winning_color = turtle.pencolor()

# #             # Display Result in a Large Font
# #             result_turtle = Turtle()
# #             result_turtle.hideturtle()
# #             result_turtle.penup()
# #             result_turtle.goto(0, -100)
# #             result_turtle.color("darkblue")
# #             result_turtle.write(
# #                 f"You {'WON!' if winning_color.lower() == user_bet.lower() else 'LOST!'}\n"
# #                 f"The {winning_color} turtle is the winner!",
# #                 align="center",
# #                 font=("Arial", 20, "bold")
# #             )

# #         random_distance = random.randint(1, 10)
# #         turtle.forward(random_distance)

# # screen.exitonclick()


# from turtle import Turtle, Screen
# import random

# # Screen Setup
# screen = Screen()
# screen.title("Turtle Race - Enhanced UI")
# screen.setup(width=600, height=400)
# screen.bgcolor("#1E1E1E")  # Dark-themed background

# # Draw Race Track
# track = Turtle()
# track.hideturtle()
# track.speed("fastest")
# track.color("white")

# # Lane Dividers
# for y in [-75, -45, -15, 15, 45, 75]:  
#     track.penup()
#     track.goto(-250, y)
#     track.pendown()
#     track.forward(500)

# # Finish Line
# finish_line = Turtle()
# finish_line.hideturtle()
# finish_line.color("white")
# finish_line.pensize(3)
# finish_line.penup()
# finish_line.goto(230, -90)
# finish_line.pendown()

# # Draw Dotted Finish Line
# for _ in range(15):
#     finish_line.forward(5)
#     finish_line.penup()
#     finish_line.forward(5)
#     finish_line_


from turtle import Turtle, Screen
import random

# Screen Setup
screen = Screen()
screen.title("Turtle Race - Enhanced UI")
screen.setup(width=600, height=400)
screen.bgcolor("#1E1E1E")  # Dark-themed background

# Draw Race Track
track = Turtle()
track.hideturtle()
track.speed("fastest")
track.color("white")

# Lane Dividers
for y in [-75, -45, -15, 15, 45, 75]:  
    track.penup()
    track.goto(-250, y)
    track.pendown()
    track.forward(500)

# Finish Line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.color("white")
finish_line.pensize(3)
finish_line.penup()
finish_line.goto(230, -90)
finish_line.pendown()

# Draw Dotted Finish Line
for _ in range(15):
    finish_line.forward(5)
    finish_line.penup()
    finish_line.forward(5)
    finish_line.pendown()

# Turtle Colors & Positions
colors = ["red", "orange", "yellow", "green", "blue"]
y_positions = [-60, -30, 0, 30, 60]

# User Bet
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win? Enter a color:")
all_turtles = []

# Create Turtles
for i in range(5):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.shapesize(1.5)  # Bigger turtles for visibility
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

# Start Race if Bet is Placed
is_race_on = bool(user_bet)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:  # When a turtle reaches the finish line
            is_race_on = False
            winning_color = turtle.pencolor()

            # Display Race Result
            result_turtle = Turtle()
            result_turtle.hideturtle()
            result_turtle.penup()
            result_turtle.goto(0, -100)
            result_turtle.color("white")
            result_turtle.write(
                f"You {'WON!' if winning_color.lower() == user_bet.lower() else 'LOST!'}\n"
                f"The {winning_color.capitalize()} Turtle is the Winner!",
                align="center",
                font=("Arial", 20, "bold")
            )

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
