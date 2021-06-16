muse = list(map(int,input().split())) 

if muse[0] != 1 and muse[0] != 8:
    print("mixed")

elif muse[0] == 1:
    for i in range(1, 7):
        if muse[i] + 1 == muse[i+1]:
            if i == 6:
                print("ascending") 
            continue
        else:
            print("mixed")
            break 
    
            
else:
    for i in range(1, 7):
        if muse[i] - 1 == muse[i+1]:
            if i == 6:
                print("descending")
            continue
        else:
            print("mixed")
            break 