N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
search_list = list(map(int, input().split()))

cnt_list = []
for i in search_list:
    cnt_list.append(card_list.count(i))
    
for i in cnt_list:
    print(i)