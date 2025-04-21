import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# 판별식 계산 (d = b^2 - 4ac)
d = b**2 - 4*a*c

#근의 공식
#(-b +- root(b^2 - 4ac))

if d > 0:
    root1 = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
    root2 = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)
    print(f"2개의 실근이 있습니다: {root1}과 {root2}")
elif d == 0:
    root = -b / (2*a)
    print(f"하나의 실근이 있습니다: {root}")
else:
    print("실근이 존재하지 않습니다.")