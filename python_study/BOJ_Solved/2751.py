N = int(input())
number_list = []

for i in range(N):
    number_list.append(int(input()))
    
number_list = sorted(number_list)

for i in range(N):
    print(number_list[i])