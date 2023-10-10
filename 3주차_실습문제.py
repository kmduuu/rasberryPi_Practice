# Practice 1
input_string = str(input(" 문자열을 입력하시오."))

vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in input_string:
    if char in vowel_counts:
        vowel_counts[char] += 1

for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")

# Practice 2
t = [[1,2], [3], [4,5,6]]
print(t)

sums = []

for listNum in t:
    total = sum(listNum)
    sums.append(total)
print(sums)

# Practice 2-1
print("두번째 방법 사용...")
t = [[1,2], [3], [4,5,6]]
def list_sum(t):
  sum = 0
  for x in t:
    for y in x:
      sum += y
  print('sum = ', sum)
list_sum(t)

# Practice 3

def palindrome(str):
    str_org = str
    while True:
        first = str[0] # S
        last = str[-1] # S

        print(first)
        print(last)

        if first != last:
            print(str_org, 'is not a palindrome!')
            return
        else:
            str = str[1:-1] # 여기서 처음과 마지막 글자가 저장된다.
            print(str)
        if len(str) <= 1:  # Check if the string is empty or has one character left.
            print(str_org, 'is a palindrome')
            return

# Test the function
input_str = "StringtS"
palindrome(input_str)

# Practice 4

# 소수 걸러내는 프로그램 1~100까지

for num in range(2, 101):
  is_prime = True
  for i in range(2,num):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    print(num, end=' ')

# Practice 5

import random
import string
from collections import defaultdict

# 랜덤한 알파벳 대문자 20개 생성
random_letters = random.choices(string.ascii_uppercase, k=20)

# 딕셔너리 초기화
letter_count = defaultdict(int)

# 알파벳 개수 세기
for letter in random_letters:
    letter_count[letter] += 1

# 결과 출력
for letter, count in letter_count.items():
    print(f"{letter}: {count}개")
    
# Practice 6

stack = []
stack_size = 5

def push(element):
    if len(stack) < stack_size:
        stack.append(element)
        print(f"Pushed {element} onto the stack.")
    else:
        print("Stack is full. Cannot push.")

def pop():
    if len(stack) > 0:
        element = stack.pop()
        print(f"Popped {element} from the stack.")
    else:
        print("Stack is empty. Cannot pop.")

while True:
    print('------------------')
    print('1. push')
    print('2. pop')
    print('3. end')
    print('------------------')
    n = int(input('input = '))

    if n == 1:
        data = int(input('Enter the data to push: '))
        push(data)
    elif n == 2:
        pop()
    elif n == 3:
        break
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')