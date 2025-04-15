import turtle

t= turtle.Turtle()
t.shape("turtle")


input_start = input("시작지점 x축과 y축 좌표를 설정하세요: ")
x1,y1 = map(int, input_start.split())

input_end = input("종료지점 x축과 y축 좌표를 설정하세요: ")
x2,y2 = map(int, input_end.split())

calculation = ((x2-x1)**2+(y2-y1)**2)**0.5

t.penup()
t.goto(x1,y1)
t.pendown()
t.goto(x2,y2)

t.write(f"점의 길이={calculation}")