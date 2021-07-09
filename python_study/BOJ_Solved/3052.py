num_list = []
per_list = []

for i in range(10):
    num_list.append(int(input()))
    per_list.append((num_list[i]) % 42)
    
per_list = set(per_list)
print(len(per_list))