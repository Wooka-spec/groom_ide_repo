N = int(input())

def one_number_check(n): #세자리 이상인 한수를 찾기위한 함수
    n_string = str(n)
    boolean = True
    gap = int(n_string[1]) - int(n_string[0])
    
    for i in range(1, len(n_string)):
        if int(n_string[i+1]) - int(n_string[i]) == gap:
            continue
        else:
            boolean = False
            break
    
    if boolean == True:
        return n

one_number_list = []
for i in range(1, N+1):
    if i < 100 :
        one_number_list.append(i)
    else:
        one_number_list.append(one_number_check(i))

print(len(one_number_list)+1)