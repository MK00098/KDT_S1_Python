import turtle
import random

# 터틀 화면 설정
screen = turtle.Screen()
screen.title("동전 던지기 게임")

# 동전 이미지 등록 (500원 앞면과 뒷면)
heads_image = "front.gif"  # 앞면 이미지 파일명
tails_image = "back.gif"   # 뒷면 이미지 파일명

# 이미지 등록
screen.addshape(heads_image)
screen.addshape(tails_image)

# 동전 터틀 생성
coin = turtle.Turtle()
coin.penup()

# 결과 표시 함수
def flip_coin():
    # 랜덤으로 앞면 또는 뒷면 선택
    result = random.choice(["앞면", "뒷면"])
    
    # 결과에 따라 이미지 변경
    if result == "앞면":
        coin.shape(heads_image)
    else:
        coin.shape(tails_image)

# 스페이스바를 눌렀을 때 동전 던지기
screen.onkeypress(flip_coin, "space")
screen.listen()

# 초기 이미지 설정
coin.shape(heads_image)

# 화면 유지
turtle.mainloop()