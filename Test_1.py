# Assignment_4  Author: Adrian Lozada
# U71130053

from ast import Num
import turtle
from tkinter import font
from random import randint

# Creates the points:
turt = turtle.Turtle(); # Creates the first turtle.
point = turtle.Turtle(); # Creates the second turtle.
ghost = turtle.Turtle(); # Creates the invisible turtle.
count = turtle.Turtle(); # Counts the number of iterations.
title9 = turtle.Turtle(); # Shows the texts for when the race starts
ender = turtle.Turtle(); # Displays the finishing texts.
lines = turtle.Turtle() # Displayes the whites lines bewteen the starting and finishing lines.

# Probabilities:
turt_prob = {
    3 : [1, 5],
    -5 : [6, 7],
    1 : [8, 10]
}
point_prob = {
    0 : [1, 4],
    7 : [5, 8],
    -10 : [9, 10],
    1 : [11, 16],
    -2 : [17, 20]
}

# Color lits;
colors = ['blue', 'green']

# Functions for the positions:
def turtm() -> int: 
    '''The function returns the movement of the turtum'''
    ran = randint(1, 10); # Creates a random num between 1 and 10.
    move = None
    for i in turt_prob: # Selects the movement for the turtle.
        if (ran >= turt_prob[i][0]) and (ran <= turt_prob[i][1]):
            move = i  
            break
    return move

def pointm() -> int:
    '''The function returns the movement of the point.'''
    ran = randint(1, 20);
    move = None
    for i in point_prob:
        if (ran >= point_prob[i][0]) and (ran <= point_prob[i][1]):
            move = i  
            break
    return move

if __name__ == "__main__":
    # Setups the track:
    # Title:
    turtle.title("Tortiose vs. Hare")

# Background color:
    turtle.bgcolor("black")

# Creates the starting and finshing line:
    ghost.shape(None);
    ghost.hideturtle();
    ghost.speed(20);
    ghost.penup();
    ghost.setpos(-100, 0);
    ghost.color("white")
    ghost.write("Start", font=('Arial', 12));
    ghost.right(90);
    ghost.pendown();
    ghost.width(3)
    for _ in range(10):
        ghost.color("orange")
        ghost.forward(6);
        ghost.color("#076EF1")
        ghost.forward(6);
    ghost.penup();
    ghost.setpos(100, -120);
    ghost.left(180);
    ghost.pendown();
    for _ in range(10):
        ghost.color("#2ED321")
        ghost.forward(6);
        ghost.color("#D321CE")
        ghost.forward(6);
    ghost.color("white")
    ghost.write("End", font=('Arial', 12));

    # Starts the race:
    turt.shape('classic')
    point.shape('turtle')
    start_1 = -100 # It starts at -100i.
    start_2 = -100
    turt.penup()
    point.penup()
    turt.speed(10)
    point.speed(10)
    turt.goto(start_1, -10)
    point.goto(start_2, -60)
    counter = 0

    # Creates whites lines:
    lines.hideturtle()
    lines.penup()
    lines.speed(20)
    lines.goto(-90, 0)
    lines.right(90)
    lines.color("white")
    var = 1
    for i in range(20):
        for n in range(5):
            lines.color(colors[var])
            lines.pendown()
            lines.forward(10)
            lines.penup()
            lines.forward(10)
            if (var == 1):
                var = 0
            elif (var == 0):
                var = 1
            
        lines.goto(-90 + i * 10, 0)
    

    # Shows the starting texts:
    title9.hideturtle()
    title9.penup()
    title9.color("white")
    title9.goto(-100, 230)
    title9.write("ON YOUR MARK...", font=("Aria", 20))
    title9.goto(-100, 200)
    title9.write("GET SET...", font=("Aria", 20))
    title9.goto(-100, 170)
    title9.write("GO 🎉", font=("Aria", 20))
    title9.goto(-100, 140)
    title9.write("AND THEY ARE OFF!! 🏃🏼", font=("Aria", 20))
    turtle.bgcolor("white")
    turtle.bgcolor("black")
    
    # Runs the race:
    while (start_1 < 100) and (start_2 < 100):
        counter += 1
        turt.speed(200)
        point.speed(200)
        adder_1 = turtm()
        adder_2 = pointm()
        start_1 += adder_1
        start_2 += adder_2
        # Returns the turtles to the beginning:
        if (start_1 < -100):
            start_1 = -100
        if (start_2 < -100):
            start_2 = -100
        # Adjusts the drawing of turt.
        if (adder_1) > 0:
            turt.color('green')
            turt.pendown()  
        elif (adder_1) < 0:
            turt.color('red')
            turt.pendown()
        # Adjusts the drawing of point.
        if (adder_2) > 0:
            point.color('green')
            point.pendown()  
        elif (adder_2) < 0:
            point.color('red')
            point.pendown()
        # Moves the turtles:    
        turt.setpos(start_1, -10)
        point.setpos(start_2, -60)
        # Writes the text on the canvas:
        count.hideturtle()
        count.color("white")
        count.penup()
        count.goto(20, -150)
        count.clear()
        count.write(f"Time of the race is {counter}", font=('Arial', 15))
            # Prints the finishing texts:
        ender.clear()
        if (start_1 > start_2):
            winner = "Hare"
        else:
            winner = "Tortiose"
        ender.hideturtle()
        ender.color('white')
        ender.penup()
        ender.setpos(150, -20)
        ender.write(f"The winner is {winner} 🏁", font=("Arial", 15))
    
    turtle.done()
else:
    turtle.done()