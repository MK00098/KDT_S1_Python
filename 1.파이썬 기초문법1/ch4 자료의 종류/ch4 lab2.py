#2 간단한 챗봇 프로그램

print('안녕하세요')

#사용자 나이 입력

name = input('이름이 뭐예요? ')

print(f'만나서 반갑습니다. {name} 님')

#이름 길이 추출

name_length = len(name)

print(f'{name} 님, 이름의 길이는 다음과 같군요: {name_length}')

#사용자 나이 입력

age = int(input('나이가 어떻게 돼요? '))

print(f'내년이면 {age+1}세가 되시는군요')
