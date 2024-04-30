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