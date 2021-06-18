test_case = []

while True:
    str_num = input()
    if str_num == "0":
        break
    test_case.append(str_num)

case_result = []
is_palindrome = True

for i in range(len(test_case)):
    if len(test_case[i]) == 1:
        case_result.append("yes")
    else:
        for j in range(int(len(test_case[i]) / 2)):
            if test_case[i][j] != test_case[i][-(j+1)]:
                is_palindrome = False
        if is_palindrome == False:
            case_result.append("no")
            is_palindrome = True
        else:
            case_result.append("yes")

for i in case_result:
    print(i)
    