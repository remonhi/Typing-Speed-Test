

# - Import modules to follow my CONVENTIONS 

import os           # for OS commands to clear the screen
import random       # for random number generation
import time         # for time functions
import turtle       # for turtle (the old Tcl/Tk) graphics
import art          # for ASCII art
import time         # for time funcdtions
from tkinter import Tk



# - Define "global" variables 

turtle_colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "brown", "black", "white", "gray", "gold", "silver",
    "darkblue", "lightgreen", "tomato", "lavender", "peachpuff",
    "deepskyblue", "forestgreen", "lightsalmon"
]

http_codes = {
    200: "OK - The request was successful.",
    201: "Created - The request was successful and a new resource was created.",
    204: "No Content - The request was successful, but there is no content to return.",
    400: "Bad Request - The server could not understand the request due to invalid syntax.",
    401: "Unauthorized - Authentication is required to access the resource.",
    403: "Forbidden - The client does not have permission to access the resource.",
    404: "Not Found - The requested resource could not be found.",
    405: "Method Not Allowed - The request method is not supported for the resource.",
    500: "Internal Server Error - The server encountered an unexpected condition.",
    502: "Bad Gateway - The server received an invalid response from an upstream server.",
    503: "Service Unavailable - The server is not ready to handle the request.",
    504: "Gateway Timeout - The server did not receive a timely response from an upstream server."
    }

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGN = "center"  # - center the text
FONT = ("Courier", 16, "normal")  # - font for the text
B = 260  # - set the boundary for the snake

#! - Clear screen fuction 

def clear_screen():
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # For macOS and Linux (posix-based systems)
        os.system('clear')

#! - Creating a random RGB color 

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


#! - Food

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-B, B)
        random_y = random.randint(-B, B)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-B, B)
        random_y = random.randint(-B, B)
        self.goto(random_x, random_y)


#! - Snake

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 20
        self.seg = []
        self.create()
        self.head = self.seg[0]

    def create(self):

        print("debug create snake")

        for i in range(0, 3):
            j = turtle.Turtle(shape="square")  # create a new turtle
            j.hideturtle()                     # make the "turle" invisible
            j.penup()                          # lift the pen up
            j.color("white")                   # set the color of the turtle
            self.seg.append(j)                 # add the turtle to the list

        for i in range(len(self.seg)):
            print(f"coordinates: {self.x}, {self.y}")
            self.seg[i].showturtle()           # show the turtle
            self.seg[i].penup()                # hide the pen
            self.seg[i].goto(self.x, self.y)
            self.x = self.x - self.size        # move down the screen

    def move(self):
        for i in range(len(self.seg)-1, 0, -1):
            new_x = self.seg[i-1].xcor()
            new_y = self.seg[i-1].ycor()
            self.seg[i].goto(new_x, new_y)
        self.seg[0].forward(self.size)

    def up(self):  # good
        print(f"heading: {self.head.heading()}")
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):  # good
        print(f"heading: {self.head.heading()}")
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):  # good
        print(f"heading: {self.head.heading()}")
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):  # good
        print(f"heading: {self.head.heading()}")
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        j = turtle.Turtle(shape="square")
        j.hideturtle()
        j.penup()
        j.color(random.choice(turtle_colors))
        self.seg.append(j)
        i = len(self.seg) - 1
        x = self.seg[i-1].xcor()
        y = self.seg[i-1].ycor()
        self.seg[i].goto(x, y)
        self.seg[i].showturtle()


#! - Scoreboard
"""
1. create a class based on Turtle ✅
2. keep track of score ✅
3. display the score using turtle.write ✅
4. use the turtle.clear method to clear the screen ✅
"""

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score} ", align=ALIGN,
                   font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", align=ALIGN,
                   font=FONT)


"""  Center Window to Display function
    - found this code at https://github.com/TomSchimansky/CustomTkinter/discussions/1820

"""
def CenterWindowToDisplay(Screen: Tk, width: int, height: int):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/1.5))
    return f"{width}x{height}+{x}+{y}"

