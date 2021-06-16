"""string = input()
num = int(input()) 

new_string = ""

for string_length in range(len(string)):
    for number in range(num):
        new_string += string[string_length]
    
print(new_string)"""

test_case = int(input()) 

test_case_string = []
for i in range(test_case):
    test_case_string.append("")
    
for cases in range(test_case):
    R, S = input().split()
    int_R = int(R)
    for S_length in range(len(S)):
        for number in range(int_R):
            test_case_string[cases] += S[S_length]
            
for new_strings in test_case_string:
    print(new_strings)