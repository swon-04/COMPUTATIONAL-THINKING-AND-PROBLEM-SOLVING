kor = int(input("국어 : "))
eng = int(input("영어 : "))
math = int(input("수학 : "))

total = kor + eng + math
print("총점 :", total)

average = total / 3
print("평균 :", average)

if average >= 80:
    print("평가 : 잘함")
elif average >= 70 and average <= 79:
    print("평가 : 보통")
else:
    print("평가 : 미흡")