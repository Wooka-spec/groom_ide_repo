N = int(input())
N_string = input()

sum_str = 0

for i in range(len(N_string)):
    sum_str += int(N_string[i])

print(sum_str)