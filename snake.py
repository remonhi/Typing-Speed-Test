

# - Import modules to follow my CONVENTIONS 

import os          # for OS commands to clear the screen
import random      # for random number generation
import time        # for time functions
import turtle      # for turtle (the old Tcl/Tk) graphics
import art         # for ASCII art
import time        # for time funcdtions
import lib         # my library of functions and variables 

# - Define "global" variables and functions.

SCREEN_SIZE = 600                   # set the screen size
BOUNDARY = abs(SCREEN_SIZE)/2 - 20  # set the boundary for the snake
title = "Snake Game"

# - Set up APIs - N/A

# - Start with my CONVENTION of introductory information  

lib.clear_screen()  # text based
print(art.text2art(title, font='medium'))

# - Setup APPLICATION LOGIC "layer" for business logic, routing, templates, etc. 

c = turtle.Screen()                             # pull up screen class from turtle module
c.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)  # set the screen size
c.bgcolor("black")                              # set the background color
c.title(title)                                  # set the title  
c.tracer(0)                                     # turning off the annimation

s = lib.Snake()              # create an instance of the Snake class
f = lib.Food()               # create an instance of the Food class         
b = lib.ScoreBoard()         # create an instance of the ScoreBoard class    

c.update()
c.listen()
c.onkey(s.up, "Up")
c.onkey(s.down, "Down")
c.onkey(s.left, "Left")
c.onkey(s.right, "Right")

#! -  Loop/play the game

game_on = True

while game_on:

    s.move()
    time.sleep(0.3)
    c.update()

    #! - module 154 | detect collision with food
    #? - see documentaion for Turtle.distance that show a Turtle object instance can be used

    if s.head.distance(f) < 15:
        f.refresh()
        s.extend()
        b.update()

    #! - module 156 | detect collision with wall

    if s.head.xcor() > BOUNDARY or s.head.xcor() < -BOUNDARY or s.head.ycor() > BOUNDARY or s.head.ycor() < -BOUNDARY:
        game_on = False
        b.goto(0, 0)
        b.write("GAME OVER", align="center", font=("Courier", 16, "normal"))

    #! - module 158 | using a slice instead

    for m in s.seg[1:]:
        if s.head.distance(m) < 10:
            game_on = False
            b.goto(0, 0)
            b.write("GAME OVER", align="center",
                    font=("Courier", 16, "normal"))


#! - making sure screen doesn't close

c.exitonclick()
