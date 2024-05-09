'''
a = 10
aa = (1, 2, 3, 4, 5)
print(type(a))
print(type(aa))

print(aa[2:4])

b = 10, 20
print(type(b))

bb = [10, 20, 30, 40, 50]

aa_1 = list(bb)
print(aa_1)

c = tuple(bb)

a = 10
type(a)
b = 10
type(b)

print(b)

a = (1, 2, 3, 4, 5)
b = (10, 20, 30, 40, 50)
print(a + b)

print(a[:])
print(a[3:])

# print(a.append(11)) 튜플은 삽입 안됨
print(a)
sum(a)
max(a)
min(a)
len(a)
# a.sort() 안됨

atuple = 10, 20, 30, 40, 50
alist = ['A', 'B', 'C']

a, b, c, d, e = atuple # 언패킹
print(a, b, c, d, e)
'''

'''
a_tuple = (4, 5, 2, 3, 8, 1, 9, 0)

x = len(a_tuple)

for i in range(x):
    print(a_tuple[:x])
    x-=1
'''

'''
adic = {
    'a' : 90,
    'b' : 70,
    'c' : 60,
    'd' : 70
}
print(adic)
adic['f'] = 100
print(adic)
del adic['f']
print(adic)
adic.clear()
print(adic)

dic_exam = {'홍길동' : '과학', '임꺽정' : '영어'}
print(dic_exam)

dic_exam['춘향이'] = '수학'
print(dic_exam)

dic_exam['홍길동'] = '체육'
print(dic_exam)

del dic_exam['춘향이']
print(dic_exam)

print(dic_exam.get('홍길동'))

print(dic_exam.values())

print(dic_exam.items())
print(tuple(dic_exam.values()))

print('홍길동' in dic_exam)
print('김길동' in dic_exam)
'''

members = {
    'choi' : 93,
    'han' : 50,
    'jung' : 92,
    'kang' : 68,
    'kim' : 80,
    'lee' : 90,
    'moon' : 65,
    'na' : 100,
    'park' : 75,
    'song' : 75
}
total = 0

for x in members.values():
    total += x

print("회원 점수 평균 =", total / len(members))