Result = list()

while True:
    A, B = map(int,input().split())
    Result.append(A+B)
    if A == 0 and B == 0:
        break
        
for i in range(len(Result)-1):
    print(Result[i])
    
