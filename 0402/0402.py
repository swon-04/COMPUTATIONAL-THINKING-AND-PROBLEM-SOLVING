'''
x = int(input("입력 : "))
if x > 0:
    print("양수")
else:
    if x == 0:
        print("0")
    else:
        print("음수")
'''
'''
score = int(input("점수 입력 >> "))
graade = ''

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("등급은", grade)
'''

'''
a = int(input("숫자를 입력하세요 >> "))
b = int(input("숫자를 입력하세요 >> "))
c = input("연사자 입력 >> ")
if c == '+':
    print(f'{a} + {b} = {a + b}')
elif c == '-':
    print(f'{a} - {b} = {a - b}')
elif c == '*':
    print(f'{a} * {b} = {a * b}')
elif c == '/':
    print(f'{a} / {b} = {a / b}')
'''

'''
ph = int(input("ph : "))
if ph >= 0 and ph <= 4:
    print("강산성")
elif ph >= 5 and ph <= 6:
    print("약산성")
elif ph == 7:
    print("중성")
elif ph >= 8 and ph <= 9:
    print("약염기성")
elif ph >= 10 and ph <= 14:
    print("강염기성")
'''

'''
year = int(input("년도 : "))

if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    print("윤년")
else:
    print("평년")
'''

'''
print("당신이 태어난 연도를 입력하세요.")
year = int(input())
age = 2020 - year + 1
if age >= 20 and age <= 26:
    print("대학생")
elif age < 20 and age >= 17:
    print("고등학생")
elif age < 14 and age >= 14:
    print("중학생")
elif age >= 8 and age < 14:
    print("초등학생")
else:
    print("학생이 아닙니다.")
'''

'''
print("두개의 양의 정수를 입력하세요:")
a = int(input())
b = int(input())
if a > b and a % 2 == 0:
    print(a, "이 큰 수이고, 짝수이다.")
elif a < b and b % 2 == 0:
    print(b, "이 큰 수이고, 짝수이다.")
'''

'''
print("3개의 양의 정수를 입력하세요:")
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("가장 큰 수는", a, "입니다.")
elif b > a and b > c:
    print("가장 큰 수는", b, "입니다.")
elif c > a and c > b:
    print("가장 큰 수는", c, "입니다.")
'''

'''
print("3개의 양의 정수를 입력하세요:")
a = int(input())
b = int(input())
c = int(input())
max = a
sum = a + b + c
if sum % 2 == 0:
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c
    print("세 수의 합은 짝수이고, 가장 큰 수는", max, "이다.")
else:
    print("세 수의 합은 홀수이고, 그 합은", sum, "이다.")
'''