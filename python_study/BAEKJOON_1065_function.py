def ap_cnt(n): # n의 각 자리 수가 등차수열인지 확인하는 함수
    if len(str(n)) <= 2:
        return True
    else:
        ap = str(n)
        cnt = 0
        ap_gap = int(ap[0]) - int(ap[1])
        for i in range(len(ap)-1):
            if int(ap[i]) - int(ap[i+1]) == ap_gap:
                continue
            else:
                return False
        return True

count = 0
N = int(input())
for i in range(1,N+1):
    if ap_cnt(i) == True:
        count += 1
    else:
        continue
        
print(count)
        
            
        
                
            
            
    