queue = []
result = []

N = int(input())
for i in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
        
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue.pop(0))
            
    elif cmd[0] == 'size':
        result.append(len(queue))
        
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
            
    elif cmd[0] == 'front':
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
            
    elif cmd[0] == 'back':
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[-1])
            
for res in result:
    print(res)