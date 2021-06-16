"""string = "OOXXOXXOOO"
cnt = 0
score = 0
score_sum = 0

for i in range(len(string)):
    if string[i] == "O":
        if cnt == 1:
            score += 1
            score_sum += score 
        else:
            cnt = 1
            score = 1
            score_sum += 1
    else:
        cnt = 0
        score = 0 
        score_sum += score 
        
print(score_sum)"""

test_cases = int(input())

OX_list = []
score_list = []

cnt = 0
score = 0
score_sum = 0

for i in range(test_cases):
    OX_list.append(input())

for j in range(test_cases):
    
    cnt = 0
    score = 0
    score_sum = 0
    
    for num in range(len(OX_list[j])):
        
        if OX_list[j][num] == "O":
            
            if cnt == 1:
                score += 1
                score_sum += score 
                
            else:
                cnt = 1
                score = 1
                score_sum += 1
                
        else:
            cnt = 0
            score = 0
        
        if num == len(OX_list[j])-1:
            score_list.append(score_sum)
            
for scores in score_list:
    print(scores)
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    