'''
# 3번 문제
a = int(input("첫 번째 정수 입력 : "))
b = int(input("두 번째 정수 입력 : "))
c = int(input("세 번째 정수 입력 : "))
min = a
if b < a and b < c:
    min = b
elif c < a and c < b:
    min = c
print("가장 작은 수 =", min)

'''

'''
# 4번 문제
menu = int(input("메뉴 선택(1:진한커피 2:연한커피) : "))
if menu == 1:
    print("진한커피를 내립니다.")
elif menu == 2:
    print("연한커피를 내립니다.")
print("잠시 기다리세요.....")
print("컵을 꺼내세요.")
'''

'''
# 5번 문제
select = int(input("도형 선택(1: 사각형, 2: 삼각형, 3: 원) : "))
if select == 1:
    w = int(input("가로 입력 : "))
    h = int(input("세로 입력 : "))
    area = w * h
    print("도형의 넓이 =", area)
elif select == 2:
    w = int(input("밑변 입력 : "))
    h = int(input("높이 입력 : "))
    area = (w * h) * 1/2
    print("도형의 넓이 =", area)
elif select == 3:
    r = int(input("반지름 입력 : "))
    area = 3.14 * r * r
    print("도형의 넓이 =", area)
else:
    print("잘못된 입력입니다.")
'''