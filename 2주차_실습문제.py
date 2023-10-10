# PDF Page 33

# Practice 1
odd = 0
for number in range(101):
    if number % 2 == 1:        
        odd = odd + number
        
print(odd) # 파이썬에서는 if문 닫을 때 들여쓰기로 한다.

# Practice 2
mltpl6 = 0
for number in range(1,101):
    if number % 6 == 0:
        mltpl6 += 1
        
print(mltpl6)

# Practice 3
r = str(input("\n문자열을 입력하시오."))
print(len(r))

# Practice 4
minority = 0
minority_list = []
print("\n소수 출력...")
for number in range(2,101):
    if (number % 2 == 1 or number == 2) and (number % 3 != 0 or number == 3) and (number % 5 != 0 or number == 5) and (number % 7 != 0 or number == 7) and (number % 9 != 0 or number == 9):
        minority_list.append(number)

print(len(minority_list))

# Practice 5
# import random as rd

# number = [1,2,3,4,5,6,7,8,9,10] # not list, dictionary...

# for _ in range(100):
#    a = rd.randint(1,10) # inside of for
#    for _ in range(number.length):

# person = {
#    "이름": "홍길동",
#    "나이": 30,
#    "직업": "개발자"
#}

# Practice 5

# histogram example...=> djEjs epdlxjrk auc qjs qkftodgoTsmswl ghkrdlsgksms rjt

import random

# 랜덤한 정수를 1부터 10까지 100번 발생시켜 리스트에 저장

random.seed(1000)

random_numbers = [random.randint(1, 10) for _ in range(100)]

# 딕셔너리를 초기화
number_counts = {}

# 각 정수의 발생 개수를 계산하여 딕셔너리에 저장
for number in random_numbers:
    if number in number_counts:
        number_counts[number] += 1 # 이미 발생한 경우
    else:
        number_counts[number] = 1 # 한 번도 발생하지 않은 경우

sorted_numbers = {key: number_counts[key] for key in range(1, 11)}

# 결과를 출력
print(sorted_numbers)