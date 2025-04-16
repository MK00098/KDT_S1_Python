#5 2050년에 나는 몇 살?
import time
now = time.time()
thisYear = int(1970+now//(365*24*3600))
print('올해는' + str(thisYear) + '년입니다.')
age = int(input('당신의 나이를 입력하세요: '))
print('2050년에는' , age+(2050-thisYear) , '살이군요.')