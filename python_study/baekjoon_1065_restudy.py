N = int(input())

cnt = 0

for i in range(1, N+1):
    if len(str(i)) <= 2:
        cnt += 1
    else:
        string_num = str(i)
        is_True = True
        gap = int(string_num[1]) - int(string_num[0])
        for j in range(2, len(string_num)):
            if int(string_num[j]) - int(string_num[j-1]) == gap:
                continue
            else:
                is_True = False
                break
        if is_True == True:
            cnt += 1
        
print(cnt)
                
            
            
