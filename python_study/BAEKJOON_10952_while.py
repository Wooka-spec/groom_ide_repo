Result = list()

while True:
    A, B = map(int,input().split())
    Result.append(A+B)
    if A == 0 and B == 0: # and 사용할때 변수 and 변수와 같이 변수에 사용X
        break
        
for i in range(len(Result)-1):
     print(Result[i])
    
