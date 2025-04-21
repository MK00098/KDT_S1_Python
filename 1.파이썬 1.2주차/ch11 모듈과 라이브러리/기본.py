# import math
# result = math.gcd(255,300)
# print(result)

# from math import *
# result = gcd(255, 300)
# print(result)

# from tkinter import *
# window = Tk()

# button = Button(window, text = '클릭하세요')
# button.pack()

# window.mainloop()
#
# from tkinter import *
# window = Tk()

# w = Label(window, text = '박스 #1', bg = 'red', fg = 'white')
# w.place (x=0, y=0)

# window.mainloop()

#
# from tkinter import*

# def to_celsius():
#     # 화씨에서 섭씨로 변환
#     temperature = float(e1.get())
#     mytemp = (temperature-32)*5/9
#     e2.delete(0, END)  # 기존 내용 삭제
#     e2.insert(0, str(mytemp))

# def to_fahrenheit():
#     # 섭씨에서 화씨로 변환
#     temperature = float(e2.get())
#     mytemp = (temperature*9/5)+32
#     e1.delete(0, END)  # 기존 내용 삭제
#     e1.insert(0, str(mytemp))

# window = Tk()

# l1 = Label(window, text='화씨', font='helvetica 16 italic')
# l2 = Label(window, text='섭씨', font='helvetica 16 italic')
# l1.grid(row=0, column=0)
# l2.grid(row=1, column=0)
# e1 = Entry(window, bg = 'green' , fg = 'yellow')
# e2 = Entry(window, bg = 'green' , fg = 'yellow')
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# b1 = Button(window, text='화씨->섭씨', command=to_celsius)
# b2 = Button(window, text='섭씨->화씨', command=to_fahrenheit)
# b1.grid(row=2, column=0)
# b2.grid(row=2, column=1)
# window.mainloop()

#

# import tkinter as tk

# def open():
#    pass

# def quit():
#    window.quit()

# window = tk.Tk()        # 윈도우를 생성합니다.

# menubar = tk.Menu(window)

# filemenu = tk.Menu(menubar)

# filemenu.add_command(label='열기', command=open)
# filemenu.add_command(label='종료', command=quit)

# menubar.add_cascade(label='파일', menu=filemenu)

# window.config(menu=menubar)
# window.mainloop()

#

# from tkinter import *

# def paint(event):
#    x1, y1 = (event.x-1), (event.y+1)
#    x2, y2 = (event.x-1), (event.y+1)
#    canvas.create_oval(x1, y1, x2, y2)

# window = Tk()
# canvas = Canvas(window)
# canvas.pack()
# canvas.bind("<B1-Motion>", paint)
# window.mainloop()