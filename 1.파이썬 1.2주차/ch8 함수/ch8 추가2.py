#추가2
#사칙연산
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input('숫자 a를 입력하시오: '))
b = float(input('숫자 b를 입력하시오: '))

print("덧셈:", add(a, b))       
print("뺄셈:", subtract(a, b))  
print("곱셈:", multiply(a, b))  
print("나눗셈:", divide(a, b))  