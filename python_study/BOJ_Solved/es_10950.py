test_cases = int(input())

plus_list = []

for cases in range(test_cases):
    plus_list.append(map(int,input().split()))  
    
for cases in range(test_cases):
    print(sum(plus_list[cases]))