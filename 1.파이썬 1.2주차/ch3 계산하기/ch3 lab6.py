#계산대 프로그램

x = int(input('투입한 돈: '))
y = int(input('물건가격 : '))

r = x - y
r500 = r // 500
r100 = (r % 500) // 100

print('거스름돈 :',r)
print('500원 동전의 개수 :',r500)
print('100원 동전의 개수 :',r100)
