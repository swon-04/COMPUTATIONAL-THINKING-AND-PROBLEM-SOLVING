from turtle import *

def avg(a, b):
    s = (a + b) / 2
    return s

# in1 = int(input("값1 : "))
# in2 = int(input("값2 : "))
# r = avg(in1, in2)
# print("평균 =", r)

# 함수문제.pdf 1번 문제
def get_max(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    
# a, b = map(int, input("두 개의 정수를 입력하시오 : ").split())
# result = get_max(a, b)
# print("두수중에서 큰수는", result, "입니다.")

# 함수문제.pdf 2번 문제
def asterisk(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()

# n = int(input("숫자입력 : "))
# asterisk(n)

# 함수문제.pdf 3번 문제
def multiple(n):
    for i in range(1, 10):
        print(n, "*", i, "=", n * i)

# n = int(input("단입력 : "))
# multiple(n)

# 함수문제.pdf 4번 문제
def total(a, b, c):
    return a + b + c

def average(a, b, c):
    return total(a, b, c) / 3

# a, b, c = map(int, input("세 과목의 점수를 입력하세요 : ").split())
# x = total(a, b, c)
# y = average(a, b, c)
# print(f"총점 : {x}, 평균 = {y}")

# 10_함수_교재.pdf 실습 10-3
def draw_circle():
    begin_fill()
    circle(100)
    end_fill()

color("yellow", "gray")

for i in range(3):
    goto(0, i * 20)
    draw_circle()