# while과 break를 사용한 정답 반복 입력
answer = "파이썬"

while True:
    user_input = input("프로그래밍 언어 중 뱀 이름이 들어간 것은? ")
    if user_input == answer:
        print("정답입니다!")
        break
    else:
        print("틀렸습니다. 다시 시도하세요.")