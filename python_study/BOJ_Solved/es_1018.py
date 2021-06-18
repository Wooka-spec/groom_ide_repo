M, N = map(int, input().split()) 

board = []
colum_list = []


for row in range(M): #입력후 2차원 배열로 리스트 생성
    colum = input()
    for colums in range(N):
        colum_list.append(colum[colums])
    board.append(colum_list)
    colum_list = []
    
#보드가 정해짐
#8*8 의 체스판 모양으로 만들어야함
#이중 반복문을 이용해서 검사해야할 모델(2차원 리스트)을 만들어(슬라이싱) 왼쪽위 색이 W일경우, B일경우를 나누어 검사하고
#최솟값을 return, 검사해야할 모델 수는 ((M-7)*(N-7))개 이므로 가장 최소값을 저장하도록 설계

def trans_list(chess_board):
    is_white = True
    if chess_board[0][0] == "B": 
        is_white = False
        
    minimum = 0
    cnt = 0
    
    chess_list_start_white = [["W", "B", "W", "B", "W", "B", "W", "B"],
                              ["B", "W", "B", "W", "B", "W", "B", "W"],
                              ["W", "B", "W", "B", "W", "B", "W", "B"],
                              ["B", "W", "B", "W", "B", "W", "B", "W"],
                              ["W", "B", "W", "B", "W", "B", "W", "B"],
                              ["B", "W", "B", "W", "B", "W", "B", "W"],
                              ["W", "B", "W", "B", "W", "B", "W", "B"],
                              ["B", "W", "B", "W", "B", "W", "B", "W"]]

    chess_list_start_black = [["B", "W", "B", "W", "B", "W", "B", "W"],
                              ["W", "B", "W", "B", "W", "B", "W", "B"],
                              ["B", "W", "B", "W", "B", "W", "B", "W"],
                              ["W", "B", "W", "B", "W", "B", "W", "B"],
                              ["B", "W", "B", "W", "B", "W", "B", "W"],
                              ["W", "B", "W", "B", "W", "B", "W", "B"],
                              ["B", "W", "B", "W", "B", "W", "B", "W"],
                              ["W", "B", "W", "B", "W", "B", "W", "B"]]
                          
    
#    for row in range(8):
#        for colum in range(8):
#            if chess_board[row][colum] != chess_list_start_white[row][colum]:
#                chess_board[row][colum] = chess_list_start_white[row][colum] 
#                cnt += 1
#    minimum = cnt
    
    cnt = 0   
    for row in range(8):
        for colum in range(8):
            if chess_board[row][colum] != chess_list_start_black[row][colum]:
                chess_board[row][colum] = chess_list_start_black[row][colum] 
                cnt += 1
                
#    if cnt > minimum:
    minimum = cnt
    return minimum #체스판의 왼쪽 끝이 W, B 두경우 일때 체스판형식으로 변경하고 두경우 중 최솟값을 반환하는 함수 
    
result_minimum = 99999
board_88_colum = []
board_88 = []
miniminmum = 0

for i in range(M-7): # 이차원 배열 슬라이싱사용해서 8*8 배열을 생성하고, trans_list 함수사용해서 리턴값의 최솟값을 저장
    for j in range(N-7):
        for k in range(8):
            board_88.append(board[i+k][j:j+8])
        print(board_88)
        if trans_list(board_88) < result_minimum:
            result_minimum = trans_list(board_88)
        board_88 = []

print(result_minimum)
    
        
        
    