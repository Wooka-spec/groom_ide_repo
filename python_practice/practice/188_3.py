limit = 10000
i = 1
sum_value = 0

while True:
    sum_value += i
    i += 1
    if sum_value > limit:
        break

    
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다".format(i-1,limit,sum_value))