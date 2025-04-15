import turtle
t=turtle.Turtle()
t.shape('turtle')

side = 100
angle = 90

for _ in range(4) :
    t.forward(side)
    t.left(angle)
    t.forward(side)
    t.left(angle)
    t.forward(side)
    t.left(angle)
    t.forward(side)

t.right(angle)
