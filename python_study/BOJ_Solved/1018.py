M, N = map(int, input().split())

board = []
Wcnt = 0
Bcnt = 0
min_num = []


for i in range(M):
    colum = input()
    colum_list = list(colum)
    board.append(colum_list)

for i in range(M-7):
    for j in range(N-7):
        Wcnt = 0
        Bcnt = 0
        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row + col) % 2 == 0:
                    if board[row][col] != 'W':
                        Wcnt += 1
                    if board[row][col] != 'B':
                        Bcnt += 1
                else:
                    if board[row][col] != 'B':
                        Wcnt += 1
                    if board[row][col] != 'W':
                        Bcnt += 1
        min_num.append(Wcnt)
        min_num.append(Bcnt)
        
print(min(min_num))  