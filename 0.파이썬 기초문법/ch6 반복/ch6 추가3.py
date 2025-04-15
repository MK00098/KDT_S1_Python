import random

# for문과 continue 사용 예시 포함
for i in range(5):  # 5번 던지기
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    
    if r1 == r2:
        print(f"두 주사위 모두 {r1}! 더블!")
        continue  # 같은 값이면 아래 문장은 건너뜀
    
    print(f"첫 번째 주사위: {r1}, 두 번째 주사위: {r2}")