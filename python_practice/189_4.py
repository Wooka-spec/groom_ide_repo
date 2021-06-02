max_value = 0
a = 0
b = 0
middle_value = 0

for i in range(1,101):
    j = 100 - i
    
    middle_value = i * j
    if middle_value > max_value:
        max_value = middle_value
        a = i
        b = j
        
print("최대가 되는 경우 : {} * {} = {}".format(a,b,max_value))
