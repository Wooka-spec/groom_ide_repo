N = int(input())
F = int(input())

N_zero = N - (N % 100)

for i in range(100):
    if N_zero % F == 0:
        break
    N_zero += 1
    
if i < 10:
    print("0", i, sep = '')
else:
    print(i)