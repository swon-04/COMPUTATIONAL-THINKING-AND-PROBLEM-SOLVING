'''
ch = input("문자 하나 입력 >> ")
print(ch)

print(ord(ch))
print(bin(ord(ch)))

a = "사과"
print(f'I think {a} is the best fruit')
b = "배"
c = 3
print("You ate %d %s today" %(c, a))

print("반지름은 %d이고, 원주율은 %.2f입니다." %(10, 3.141592))
'''
# 20233128 김성원
'''
kor = int(input("국어 점수 입력 >> "))
math = int(input("수학 점수 입력 >> "))
eng = int(input("영어 점수 입력 >> "))

sum = kor + math + eng
avg = sum / 3

print("총점 : %d" %sum)
print("평균 : %.2f" %avg)

r = float(input("반지름 입력 >> "))
s = r * r * 3.14
print("원의 넓이 : ", s)

n1 = int(input("숫자1 : "))
n2 = int(input("숫자2 : "))

print(f'{n1} / {n2} = {n1 / n2}')
print(f'{n1} // {n2} = {n1 // n2}')
print(f'{n1} % {n2} = {n1 % n2}')

'''
second = int(input("초 : "))
a = second // 60
b = second % 60
# print(f'{second}초 = {a}분 {b}초')
print(second, "초 = ", a, "분 ", b, "초")
