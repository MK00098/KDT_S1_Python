##정수의 종류를 판별하는 스마트 터틀
#사용자로부터 정수를 입력 받음
#양의 정수, 0, 음의 정수 판단 후 이동 및 텍스트 쓰기
#(100,100), (100,0), (100,-100)

#turtle 라이브러리 기본 세팅
import turtle
t=turtle.Turtle()
t.shape('turtle')

#사용자로부터 정수 입력 받기
num = int(turtle.textinput('python turtle graph','숫자를 입력하시오: '))

if num > 0 :
    t.goto(100,100)
    t.write('입력된 정수는 양의 정수입니다.')
    
elif num == 0 :
    t.goto(100,0)
    t.write('입력된 정수는 0입니다.')

else :
    t.goto(100,-100)
    t.write('입력된 정수는 음의 정수입니다.')

turtle.done()