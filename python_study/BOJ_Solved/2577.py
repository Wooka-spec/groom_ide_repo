A = int(input())
B = int(input())
C = int(input())

str_num = list(str(A * B * C))
cnt_list = []

for i in range(10):
    cnt = str_num.count(str(i))
    cnt_list.append(cnt)

for i in range(10):
    print(cnt_list[i])