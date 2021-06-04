def bridge_cases(N,M):
    if N == M:
        return 1
    else:
        reminder = M-N
        for i in range(1,reminder):
            