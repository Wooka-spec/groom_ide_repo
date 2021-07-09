num_list = list(map(int, input().split()))

sum_n = 0

for i in num_list:
    sum_n += i ** 2
    
print((sum_n) % 10)
    