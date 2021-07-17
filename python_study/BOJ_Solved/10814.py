N = int(input())
members_data = []

for i in range(N):
    member = []
    age, name = input().split()
    age = int(age)
    
    member.append(age)
    member.append(name)
    members_data.append(member)
    
members_data.sort(key = lambda member : (member[0]))

for member in members_data:
    print(member[0], member[1])
