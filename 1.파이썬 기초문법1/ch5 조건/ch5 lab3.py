##주민등록번호의 의미
#주민등록번호 뒷자리 첫 숫자 입력
num = int(input('주민등록번호의 성별 정보 번호를 생성합니다.'))
print('생성번호 :',num)

if num == 1 or num == 3 :
    print('남성입니다.')

elif num == 2 or num == 4 :
    print('여성입니다.')

print('프로그램을 종료합니다.')