string = input().lower()
string_set = list(set(string))
cnt = []

for word in string_set:
    count = string.count(word)
    cnt.append(count)
    
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(string_set[(cnt.index(max(cnt)))].upper())