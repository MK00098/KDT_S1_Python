#BMI 계산기
def calculate_bmi(weight, height): #BMI 계산 함수
    height_m = height / 100  # cm → m 변환
    bmi = weight / (height_m ** 2)  # BMI 계산 공식
    return bmi

def bmi_status (weight, height) : #BMI에 따른 건강상태 계산 함수
    bmi = calculate_bmi(weight, height)

    if bmi < 18.5:
        return "저체중입니다."
    elif bmi < 25:
        return "정상 체중입니다."
    elif bmi < 30:
        return "과체중입니다."
    else:
        return "비만입니다."
    
# 예시 호출
weight = 47
height = 160

print("당신의 BMI는", calculate_bmi(weight, height), "입니다.")
print("건강 상태:", bmi_status(weight, height))