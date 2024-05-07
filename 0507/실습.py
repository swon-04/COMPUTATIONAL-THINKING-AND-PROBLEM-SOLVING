seat = [ ]

for i in range(10):
    seat.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

while True:
    print("="*30)
    print("\t  좌석 번호")
    seat_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(seat_list)
    print("="*30)

    for i in range(10):
        print(seat[i])

    row = int(input("원하시는 좌석의 행번호를 입력하세요(종료는 -1) "))
    col = int(input("원하시는 좌석의 열번호를 입력하세요(종료는 -1) "))

    if row == -1 or col == -1:
        print("종료!")
        break
    seat[row][col] = 1