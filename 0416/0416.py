# test
'''
i = 0
while i < 5:
    print("환영합니다.")
    i += 1
print("반복이 종료되었습니다.")
'''

'''
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
'''

'''
i = 1
x = 0
while i < 11:
    x += i
print("합계", x)
'''

'''
a = int(input("숫자 입력 >> "))
result = 0
for i in range(a, 0, -1):
    result += i
    a -= 1
print(result)
'''

'''
i = 1
while i < 10:
    print("3 *", i, "= ", 3 * i)
    i += 1
'''

'''
for y in range(5):
    for x in range(10):
        print("*", end="")
    print()
'''

'''
# 중첩반복문예제 1
a = int(input("단 : "))
for i in range(10):
    print(f"{a} * {i} = {a * i}")
'''

'''
# 중첩반복문예제 2
for i in range(5):
    for j in range(1, 5):
        print(j, end="")
    print()
'''

'''
# 중첩반복문예제 3
a = 1
for i in range(5):
    for j in range(a):
        print("*", end="")
    a += 1
    print()
'''

'''
# 중첩반복문예제 4
x = int(input("밑변, 높이 : "))
a = 1

for x in range(x):
    for j in range(a):
        print("*", end="")
    a += 1
    print()
'''