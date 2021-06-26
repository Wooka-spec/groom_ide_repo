test_case = []

for i in range(int(input())):
    case = list(map(int, input().split()))
    test_case.append(case)
    
f = 0
ho = 0

for i in range(len(test_case)):
    if test_case[i][2] % test_case[i][0] == 0:
        f = test_case[i][0] * 100
        ho = test_case[i][2] // test_case[i][0]
    else:
        f = (test_case[i][2] % test_case[i][0]) * 100
        ho = test_case[i][2] // test_case[i][0] + 1
    print(f + ho)