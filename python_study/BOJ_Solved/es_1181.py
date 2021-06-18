voca_list = []

voca_count = int(input())

for cnt in range(voca_count):
    voca_list.append(input())
    
set_list = set(voca_list)
voca_list = list(set_list)

voca_len_list = []
sorted_voca_list = []


for i in range(1,51):
    voca_len_list = [j for j in voca_list if len(j) == i]
    voca_len_list.sort()
    sorted_voca_list.append(voca_len_list)
    voca_len_list = []

result_voca_list = []
    
for i in range(len(sorted_voca_list)):
    result_voca_list += sorted_voca_list[i]
    
for cnt in range(len(result_voca_list)):
    print(result_voca_list[cnt])