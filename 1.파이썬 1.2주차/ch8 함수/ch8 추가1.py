#추가1
#1.f(x) = x*x + 1 정의하기
#2.x를 0부터 150까지 변화시키며 계산하기
#3도출된 값으로 turtle을 활용하여 그래프 그리기

import turtle

# 함수 정의
def f(x):
    return x ** 2 + 1

# 거북이 설정
t = turtle.Turtle()
t.speed(0)
t.shape('turtle')

# x축 그리기
t.up()
t.goto(0, 0)
t.down()
t.goto(160, 0)

# y축 그리기
t.up()
t.goto(0, 0)
t.down()
t.goto(0, 250)

# 함수 그래프 그리기
t.penup()
for x in range(0, 150+1):
    y = f(x) * 0.01  # 축소 비율 적용
    t.goto(x, y)
    t.down()

turtle.done()
