def d(n):
    if n > 0 and n <100:
        Result_sumnum = n + n // 10 + n % 10
    elif n >= 100 and n < 1000:
        Result_sumnum = n + n // 100 + (n // 10) % 10 + n % 10
    elif n >= 1000 and n < 10000:
        Result_sumnum = n + n//1000 + (n//100) % 10 + (n//10) % 10 + n % 10
    return Result_sumnum

for i in range(1,10001):
    cnt = 0
    for j in range(1,i):
        if d(j) == i:
            cnt += 1
    if cnt >= 1:
        continue
    else :
        print(i)
        
#시간초과
        
    