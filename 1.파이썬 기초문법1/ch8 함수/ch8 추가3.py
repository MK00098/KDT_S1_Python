#추가3
#소수 = 1보다 크고, 1과 자기 자신만 약수인 수

#소수 판별 함수 만들기
def testprime(n): #testprime() 정의
    if n < 2:       #소수는 2부터 시작
        return False
    for i in range(2, n): #2부터 n-1까지
        if n % i == 0: #2부터 n-1까지의 숫자들로 나눠지는 수가 있다면면
            return False
    return True #없다면 소수!

#2부터 100까지 소수만 출력
for i in range(1, 101):
    if testprime(i):
        print(i, end=' ') #한 칸씩 띄워서 표시시