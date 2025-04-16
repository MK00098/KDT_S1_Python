import turtle as t

t.speed(0)  # 빠르게 그리기

for i in range(6):  # 6개의 방향
    t.forward(100)
    t.backward(100)
    t.left(60)

t.done()