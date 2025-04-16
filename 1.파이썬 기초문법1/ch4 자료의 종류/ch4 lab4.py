#암호 프로그램 만들기

#사용자로부터 평문 입력 받기기
plain_text = input('평문을 입력하세요 : ')

#문자열을 거꾸로 배치하여 암호문 생성하기
cipher_text = plain_text[::-1]

print(f'평문: {plain_text}')
print(f'암호문: {cipher_text}')