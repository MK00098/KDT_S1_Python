import random

values = []  # 빈 리스트 생성
for _ in range(10):  # 10번 반복
    values.append(random.randint(1, 100))  # 1~100 사이의 난수를 리스트에 추가

print(values)  # 생성된 리스트 출력