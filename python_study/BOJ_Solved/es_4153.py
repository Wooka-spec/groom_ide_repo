test_case = []

while True:
    case = list(map(int, input().split()))
    if case[0] == 0 and case[1] == 0 and case[2] == 0:
        break
    test_case.append(case)
    case = []

for i in range(len(test_case)):
    max_value = max(test_case[i])
    test_case[i].remove(max_value)
    if max_value ** 2 == test_case[i][0] ** 2 + test_case[i][1] ** 2:
        print("right")
    else:
        print("wrong")