#heroes = ['아이언맨', '토르', '헐크', '스칼렛 위치']

#numbers = [7, 12, 33, 777]

#slist =['영어' , '수학' , '사회', '과학']
#print(slist)

#cart = []
#cart.append('사과')
#cart.append('세제')
#print(cart)

#slist = ['영어' ,'수학' , '사회' , '과학']
#print(slist[3])

#letters = ['A', 'B', 'C', 'D', 'E', 'F']
#print(letters[-1:-6:-1])

#letters = ['A', 'B', 'C', 'D', 'E', 'F']
#copy = letters[:]
#print(copy)

#cart = ['사과', '세제', '화장지', '치약']
#cart[5] = '섬유 유연제'
#print(cart)

#append
#cart.append('양말')

#insert
#cart.insert(1, '건전지')

#remove
#cart.remove('화장지')
#if '화장지' in cart:
#    cart.remove('화장지')

#del
#del cart[2]

#pop() = 리스트 마지막 항목 삭제
#cart = ['사과','세제','화장지','치약']
#item = cart.pop()
#print(cart)
#print(item)

#index() = 리스트 항목 탐색
#if '화장지' in cart:
#    print(cart.index('화장지'))

#sorting = 리스트 정렬
#sort() = 오름차순 정렬렬
heroes = ['아이언맨', '토르', '헐크', '스칼렛 위치']
#heroes.sort()
#print(heroes)

#sort(reverse = Ture) = 내림차순 정렬
#heroes.sort(reverse = True)
#print(heroes)

#new_heroes = sorted(heroes)
#print(heroes)
#print(new_heroes)

#2차원 리스트 = [[]] 활용
#num = [[10, 20, 30], [40, 50, 60]]
#print(num[0][1])
#[1][2] 100으로 바꾸기기
#num[1][2] = 100
#print(num)

#리스트 + 반복문(for in) 활용
#for i in [1,2,3]:
#    print('i=',i)

#heroes = []
#for i in range(5):
#    name = input('영웅들의 이름을 입력하시오: ')
#    heroes.append(name)

#for i in heroes:
#    print(i, end=" ")

num = [100, 96, 209, 22, 30, 117]
for i in num:
    if i % 2 == 1:
        print(i, end=" ")