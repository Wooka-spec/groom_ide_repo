M, N = map(int, input().split())

chess_board = []
colums = []

for row in range(M):
    colum_str = input()
    for colum in range(N):
        colums.append(colum_str[colum])
    chess_board.append(colums)
    colums = []
    
test_chess_board = []
    
for start_row in range(M-7):
    for start_colum in range(N-7):
        for make_board in range(8):
            