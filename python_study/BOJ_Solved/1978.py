N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

cnt = 0

for num in A:
    if num < 2:
        continue
    error = 0
    for i in range(2, num):
        if num % i == 0:
            error += 1
            continue
    if error == 0:
        cnt += 1
            
    
print(cnt)