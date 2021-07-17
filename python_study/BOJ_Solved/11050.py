def factorial(I):
    result = 1
    for i in range(2, I+1):
        result *= i
    return result
    

N, K = map(int, input().split())
BC = factorial(N) / (factorial(N - K)*factorial(K))
print(int(BC))

    