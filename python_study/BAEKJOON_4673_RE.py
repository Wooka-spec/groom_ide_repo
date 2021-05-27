def d(n):
    result = n
    for i in list(str(n)):
        result += int(i)
    return result

remove_num = []
for cnt in range(10001):
    remove_num.append(d(cnt))

for cnt in range(1,10000):
    if cnt in set(remove_num):
        continue
    else:
        print(cnt)