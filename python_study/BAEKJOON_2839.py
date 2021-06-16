N = int(input())

bag = 0
if N % 5 == 0:
    print(N // 5)
elif N % 5 != 0:
    if (N % 5) % 3 == 0:
        print((N // 5) + ((N % 5) // 3))    
    else:
        if N % 3 == 0:
            print(N // 3)
        else:
            print(-1)