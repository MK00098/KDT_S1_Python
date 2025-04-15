# 사용자로부터 구구단의 단수를 입력받기
dan = int(input("구구단의 단수를 입력하세요 (1~9): "))

# 입력받은 단수에 대해 구구단 출력
if 1 <= dan <= 9:  # 입력값이 1부터 9 사이인지 확인
    print(f"{dan}단:")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
else:
    print("1과 9 사이의 숫자를 입력해주세요.")
