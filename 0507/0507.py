numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[::-1])

print() # 줄바꿈

lst = [1, 2, 3, 4, 5, 6, 7, 8]
#lst[0:3] = ['white', 'blue', 'red']
#lst[::2] = [99, 99, 99, 99]
#lst[:] = []
print(lst)

print() # 줄바꿈

numbers = list(range(0, 10))
print(numbers)
del numbers[-1]
print(numbers)

print() # 줄바꿈

s = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print(s)
rows = len(s)
cols = len(s[0])

for r in range(rows):
    for c in range(cols):
        print(s[r][c], end=",")
    print()

print() # 줄바꿈

transposed = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("원래 행렬 =", matrix)

for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print("전치 행렬 =", transposed)