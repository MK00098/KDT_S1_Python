#기본 입력함수
# input -> print
#파일 입력함수
# file
# infile = open("D:\code\mk00098\DREAM2기_김문기\ch10 파일 입출력\실습용 파일.txt" , "r", encoding="utf-8")
# lines = infile.readlines()
# print(lines)
# infile.close()
# infile = open("D:\code\mk00098\DREAM2기_김문기\ch10 파일 입출력\실습용 파일.txt" , "r", encoding="utf-8")

# line1 = infile.readline()
# print(line1)

# line2 = infile.readline()
# print(line2)

# infile.close()
# outfile = open("D:\code\mk00098\DREAM2기_김문기\ch10 파일 입출력\실습용 파일.txt" , "a", encoding="utf-8")

# outfile.write('전우치2 010-1234-8989\n')

# outfile.close()
# a = "All's well that ends well"

# print(a.split())

# import csv
# f = open("D:\code\mk00098\DREAM2기_김문기\ch10 파일 입출력\input.csv" , "r")
# data = csv.reader(f)

# for line in data :
#     print(line)

# f.close()

# # 파일 경로 지정
# input_file = "d:Wphones.txt"  # 입력 파일 경로
# output_file = "d:Wtemp.txt"   # 출력 파일 경로

# # 입력 파일 열기
# infile = open("D:\code\mk00098\DREAM2기_김문기\ch10 파일 입출력\input.txt", "r",
# encoding="utf-8")

# # 파일 전체 내용 읽기
# content = infile.read()

# # 입력 파일 닫기
# infile.close()

# # 출력 파일 열기
# outfile = open(output_file, "w", encoding="utf-8")

# # 읽은 내용을 출력 파일에 쓰기
# outfile.write(content)

# # 출력 파일 닫기
# outfile.close()

# print("파일 복사가 완료되었습니다.")

#

# 파일 열기
infile = open("D:\code\mk00098\DREAM2기_김문기\ch10 파일 입출력\input.txt", "r", encoding="utf-8")
#infile = open('경로', 'r' , encoding="utf-8")
# 파일 내용 읽기
content = infile.read()

# 파일 닫기
infile.close()

# 단어 분리를 위해 특수문자 처리
import string
for char in string.punctuation:
    content = content.replace(char, ' ')

# 모든 문자를 소문자로 변환
content = content.lower()

# 단어로 분리
words = content.split()

# 단어 빈도 분석
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# 빈도 내림차순으로 정렬
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# 결과 출력
print("\n가장 많이 사용된 단어(상위 10개):")
for word, count in sorted_words[:10]:
    print(f"{word}: {count}회")