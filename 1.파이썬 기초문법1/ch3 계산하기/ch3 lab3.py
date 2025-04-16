x1=int(input('x1의 좌표를 입력하시오: '))
y1=int(input('y1의 좌표를 입력하시오: '))
x2=int(input('x2의 좌표를 입력하시오: '))
y2=int(input('y2의 좌표를 입력하시오: '))

d=((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5

print('x1:' , x1)
print('y1:' , y1)
print('x2:' , x2)
print('y2:' , y2)
print('두 점 사이의 거리 =',d)
