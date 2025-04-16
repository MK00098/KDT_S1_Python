#딕셔너리
#key - value 구조 { }로 표시시
#phone_book = {'홍길동': '010-1234-5678',
              #'강감찬': '010-1111-2222',
              #'이순신': '010-3333-4444'}
#print(phone_book['강감찬'])
#출력 정리
#for key in sorted(phone_book.keys()):
#    print(key,phone_book[key])

#keys, values 탐색
#print(phone_book.keys())

#clear
#phone_book.clear()
#print(phone_book)

#english_dict = {}
#english_dict['one'] = '하나'
#english_dict['two'] = '둘'
#english_dict['three'] = '셋'

#word = input('단어를 입력하시오: ')
#print(english_dict[word])

#english_dict = dict()
#print(dict)

#편의점 재고 관리 프로그램
#items = {'커피':7, '펜':3, '종이컵':10, '우유':5, '콜라':4, '라면':11}

#print('판매 전 재고', items)

#sell = input('판매한 물건을 입력하세요: ')

#if sell in items :
#    items[sell]-= 1
#else :
#    print('판매 제품이 아닙니다')

#print('판매 후 재고', items)

#반복문과 딕셔너리의 items()를 이용하여 key와 value를 동시 출력
#phone_book = {'홍길동': '010-1234-5678',
#              '강감찬': '010-1111-2222',
#              '이순신': '010-3333-4444'}
#for k, v in phone_book.items():
#    print('{}의 전화번호는 {}입니다.'. format(k,v))

#집합 set() / {}활용
s=set()
s={1, 2, 5}

#add discard remove clear
s.add(10)
print(s)

s.discard(5)
print(s)

s.remove(2)
print(s)

s.clear()
print(s)