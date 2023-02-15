import turtle
import pandas as pd
from tkinter import *
from tkinter import messagebox
import random

screen = turtle.Screen()
screen.title("US States Games")
screen.addshape(name="blank_states_img.gif")
turtle.shape("blank_states_img.gif")

correct_guesses = 0
new_state = turtle.Turtle(visible=False)
data = pd.read_csv("50_states.csv")
states_to_learn = data["state"].tolist()
guessed_states = []

while correct_guesses < 50:

    answer = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="Enter a state name")

    if answer is None:
        for row in states_to_learn:
            new_state.penup()
            new_state.goto(float(data[data["state"] == row]["x"]),
                           float(data[data["state"] == row]["y"]))
            new_state.pencolor("red")
            new_state.write(row)
        with open('states_to_learn.txt', 'w') as f:
            for row in states_to_learn:
                f.write(f"{row}\n")
        correct_guesses = 60
        messagebox.showinfo(title="Game over", message="You lost.")

    else:
        tanswer = answer.title()
        for row in data["state"]:
            if tanswer == row:
                if guessed_states.count(tanswer) < 1:
                    guessed_states.append(tanswer)
                    new_state.penup()
                    new_state.goto(float(data[data["state"] == tanswer]["x"]),
                                   float(data[data["state"] == tanswer]["y"]))
                    new_state.write(tanswer)
                    correct_guesses += 1
                    if states_to_learn.count(tanswer) > 0:
                        states_to_learn.remove(tanswer)
                else:
                    for state in guessed_states:
                        if tanswer == state:
                            messagebox.showwarning(title="Warning",
                                                   message="You already correctly guessed that state! Try again.")

if correct_guesses == 50:
    screen.title("CONGRATULATIONS, YOU WIN!")

    screen.colormode(255)

    t = turtle.Turtle(visible=False)
    t.speed(0)

    t.color("red")

    for i in range(10):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        t.penup()
        t.goto(x, y)
        t.pendown()

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.color(r, g, b)

        size = random.randint(30, 200)
        for i in range(36):
            t.forward(size)
            t.backward(size)
            t.left(10)

screen.bye()