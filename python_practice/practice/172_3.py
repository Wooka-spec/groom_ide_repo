numbers=list(map(int,input().split()))
counter={}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1
        
print(counter)