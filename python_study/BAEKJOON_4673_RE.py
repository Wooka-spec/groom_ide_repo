def d(n):
    next_n = n
    for str_num in str(n):
        next_n += int(str_num)
    return next_n

remove_num = []
for num in range(10001):
    remove_num.append(d(num)) # 1~10000까지 d(n) 함수에 넣어 셀프넘버가 아닌 수를 remove_num 리스트에
    
for num in range(10001):
    if num in set(remove_num):
        continue
    else:
        if num > 10000:
            continue
        else:
            print(num)
