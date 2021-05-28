A, B, V = map(int,input().split())

climb_high = 0
day = 0
while True:
    day +=1
    climb_high += A
    if climb_high >= V:
        print(day)
        break
    climb_high -= B
