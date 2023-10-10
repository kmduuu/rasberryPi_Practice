import math

print("hello, world!");

print('{:.2f}'.format(3.14159))
print('{:.2f} {:.4f}'.format(3.14159, 3.14159))

a = 12

str = 'myString'
print(str)
print(len(str))

print(str[2])
a = str[3]
b = str[-1]

str1 = "My name is {fname}, I'm {age}.".format(fname='John', age = 35)
print(str1)
str3 = "My name is {}, I'm {}.".format('John', 35)
print(str3)

print('a' * 3)

# 1.
r = float(input("반지름을 입력하시오.\n"))
program1 = r * r * math.pi
print(program1)

# 2.
c = float(input("섭씨 온도를 입력하시오.\n"))
program2 = c * (9/5) + 32
print(program2)

myList = [1,2,3,4,5]
myList2 = []
myList3 = list()
print(myList[0], myList[4])

myList4 = [1,2,3,'k','string',[10,20,30]]

list1 = [1,2,3]
list2 = [4,5,6]
list_list = [list1, list2]

print(list_list)

print(list_list[0])
print(list_list[0][0])
print(list_list[1][2])

myList = [[1,2,3],4,5,6]
print(myList[0])
print(myList[0][1])
print(myList[-1])
print(myList[-2])

# Practice 3

grade = int(input("성적을 입력하시오."))
if grade >= 90:
        print("A")
    
elif grade >= 80 and grade < 90:
        print("B")
    
elif grade >= 70 and grade < 80:
        print("C")
    
elif grade >= 60 and grade < 70:
        print("D")
    
else:
        print("F")

# Practice 4
# Use sort function...

a = int(input("첫번째 변수를 입력하시오."))
b = int(input("두번째 변수를 입력하시오."))
c = int(input("세번째 변수를 입력하시오."))

variables = [a,b,c]

variables.sort()

print("Variable : ")
for var in variables:
    print(var)

# Use If function...

a = int(input("첫번째 변수를 입력하시오."))
b = int(input("두번째 변수를 입력하시오."))
c = int(input("세번째 변수를 입력하시오."))

if a <= b <= c:
    print(c)
    print(b)
    print(a)
elif a <= c <= b:
    print(b)
    print(c)
    print(a)
elif b <= a <= c:
    print(c)
    print(a)
    print(b)
elif b <= c <= a:
    print(a)
    print(c)
    print(b)
elif c <= a <= b:
    print(b)
    print(a)
    print(c)
elif c <= b <= a:
    print(a)
    print(b)
    print(c)
