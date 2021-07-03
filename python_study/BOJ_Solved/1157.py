N = int(input())

score_list = input().split()
for i in range(N):
    score_list[i] = int(score_list[i])
high_score = max(score_list)
sum_score = 0

for i in score_list:
    sum_score += i/high_score*100
    
print(sum_score / 3)