#3 거북이와 인사해봐요

import turtle #turtle 그래픽 모듈
import time #시간 지연을 위한 모듈

#사용자 이름 입력

name = turtle.textinput('거북이와 인사', '당신의 이름을 입력하세요:')

# 거북이 설정

t= turtle.Turtle()
t.shape('turtle')
t.speed(1) #거북이 속도 설정

#인사 메시지 출력
t.up()
t.goto(-65,0) #글자가 중앙에 놓이도록 거북이 위치 조정
t.down()
t.write(f'{name}님, 만나서 반가워요!')

# 잠시 기다렸다가 사각형 그리기
time.sleep(1)
t.up()
t.goto(-100, -50)
t.down()

# 사각형 그리기
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
