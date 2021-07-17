from collections import deque

deq = deque()
result = []

N = int(input())
for i in range(N):
    cmd = input().split()
    
    if cmd[0] == 'push_front':
        deq.appendleft(cmd[1])
    
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
        
    elif cmd[0] == 'pop_front':
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq.popleft())
    
    elif cmd[0] == 'pop_back':
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq.pop())
            
    elif cmd[0] == 'size':
        result.append(len(deq))
        
    elif cmd[0] == 'empty':
        if len(deq) == 0:
            result.append(1)
        else:
            result.append(0)
        
    elif cmd[0] == 'front':
        result.append(deq[0])
        
    elif cmd[0] == 'back':
        result.append(deq[-1])
        
for res in result:
    print(res)