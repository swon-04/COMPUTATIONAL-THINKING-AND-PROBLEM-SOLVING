'''
b1 = 234
b2 = 82
b3 = 128
b4 = 50
b5 = 165

total = b1+b2+b3+b4+b5
print("판매 수량 합계 =", total)
print("판매 수량 평균 =", total/5)

books = [234, 82, 128, 50, 155]
total = 0

for x in books:
    total += x
print("판매 수량 합계 =", total)
print("판매 수량 평균 =", total/len(books))
'''

'''
bb = []
bb.append(10)
bb.append(20)
bb.append(30)
print(bb)
bb.append("sw")
print(bb)
bb.insert(0, "김조선")
print(bb)
bb.remove(30)
print(bb)
del bb[0]
print(bb)
bb.pop()
print(bb)
bb.clear()
print(bb)
'''

'''
cc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cc[0:3])
print(cc[:3])
print(cc[:])
print(cc[5:])
print(cc[5:8])
'''