N, M = map(int, input().split())
card_int = list(map(int, input().split()))

max_sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card_int[i] + card_int[j] + card_int[k] > M:
                continue 
            else:
                max_sum = max(max_sum, card_int[i] + card_int[j] + card_int[k])
print(max_sum)
    