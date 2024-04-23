'''
for x in range(5):
    print(x, "환영합니다.")

sum = 0
n = int(input("숫자 입력 >> "))
for x in range(n + 1):
    sum = sum + x
print(sum)
'''

'''
n = int(input("어디까지 계산할까요 >> "))
sum = 0
for i in range(n + 1):
    sum = sum + i
print(f'1부터 {n}까지의 정수의 합 = {sum}')
'''

'''
n = int(input("정수 입력 >> "))
sum = 1
for i in range(1, n+1):
    sum = sum * i
print(f'{n}!은 {sum}이다.')
'''

'''
a = 0
b = 0
for i in range(101):
    if i % 2 == 0:
        b += i
    else:
        a += i
print("홀수 합 :", a)
print("짝수 합", b)
'''

sum = 0
for i in range(3, -4, -1):
    print(i, end=" ")
    sum += i
print(f'\n{sum}')