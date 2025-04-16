import turtle

def draw_square(x, y, c):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(c)
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

t = turtle.Turtle()
t.shape('turtle')
colors = ["yellow", "red", "purple", "blue"]  # 리스트에 색 저장

x, y = -150, 0
for c in colors:
    draw_square(x, y, c)
    x += 50  # x 좌표 이동해서 겹쳐 그리기

turtle.done()