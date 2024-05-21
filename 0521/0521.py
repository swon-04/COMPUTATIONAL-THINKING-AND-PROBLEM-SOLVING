def fpython():
    print("Python")
    print("파이썬")

def ifpython():
    print("Python")

def print19():
    for i in range(1, 10):
        print(i, end=" ")
    print("")

def fadd1(n, m):
    s = n + m
    print(n, "+", m, "=", s)

# a = 3
# b = 4
# fadd1(a, b)

def calc_gugudan(dan):
    if dan>=1 and dan<=9:
        for i in range(1, 10):
            print(dan, "*", i, "=", dan*i, "") 
    else:
        print("단은 1~9까지 입력해주세요.")

# d = int(input("단 : "))
# calc_gugudan(d)

def print_se(start, end):
    if start < end:
        for i in range(start, end+1):
            print(i, end=" ")
        print("")

# s = int(input("시작 >> "))
# e = int(input("끝 >> "))
# print_se(s, e)

def fadd2(n, m):
    s = n + m
    return s

a = 3
b = 4
r =fadd2(a, b)
print("반환값 =", r)