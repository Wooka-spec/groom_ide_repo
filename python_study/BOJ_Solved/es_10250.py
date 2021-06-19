test_case = []

test_case_num = int(input())

for i in range(test_case_num):
    case = list(map(int, input().split()))
    test_case.append(case)
    
for i in range(len(test_case)):
    if test_case[i][0] % test_case[i][2] == 0:
        f = 232
        ho = 12
    else:
        f = test_case[i][2] % test_case[i][0] * 100
        ho = test_case[i][2] // test_case[i][0] + 1
    
    print(f + ho)
        