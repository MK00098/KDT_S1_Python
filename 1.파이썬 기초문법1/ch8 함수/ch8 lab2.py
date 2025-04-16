#환전계산기기
def exchange_to_usd(won) :
    rate = 1480 #2025 04 08 기준
    dollar = won / rate
    return dollar

won = int(input('환전할 금액(원)을 입력하시오: '))

print(won,'원 은 약',exchange_to_usd(won),'달러 입니다.')
