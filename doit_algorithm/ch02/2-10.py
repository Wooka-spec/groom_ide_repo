ptr = 0
counter = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] ** 2 <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1
        
for i in range(ptr):
    print(prime[i])
print('나눗셈을 실행한 횟수> %d' %counter)