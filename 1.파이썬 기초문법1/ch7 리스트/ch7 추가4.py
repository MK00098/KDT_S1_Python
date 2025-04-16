import turtle
import random

s = turtle.Screen()
s.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")

def draw_star(color, length, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()

colors = ["yellow", "green", "skyblue", "blue", "orange", "white"]

for j in range(3):
    for color in colors:
        length = random.randint(10, 150)
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        draw_star(color, length, x, y)