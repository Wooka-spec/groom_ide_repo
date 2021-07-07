N = int(input())
A = list(map(int, input().split()))
M = int(input())
search_num = list(map(int, input().split()))
A = sorted(A)


for i in range(len(search_num)):
    pl = 0
    pr = len(A) - 1
    boolean = 1
    
    while True:
        pc = (pl + pr) // 2
        if search_num[i] == A[pc]:
            print(1)
            boolean = 0
            break
        elif search_num[i] < A[pc]:
            pr = pc - 1
        else:
            pl = pc + 1
        if pl > pr:
            break
    if boolean == 1:
        print(0)
    