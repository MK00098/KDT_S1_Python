country = input("국가를 입력하세요: ")
region = input("도를 입력하세요: ")

if country != "한국":
    print("배송료는 20000원입니다.")
elif region == "제주도":
    print("배송료는 10000원입니다.")
else:
    print("배송료는 5000원입니다.")