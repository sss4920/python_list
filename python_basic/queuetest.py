import sys
from collections import deque
queue = deque([])
input=sys.stdin.readline
def empty(queue):
    if len(queue)==0:
        return 1
    else:
        return 0
n = int(input())
for _ in range(n):
    command = input().split()
    if len(command)>=2:
        queue.append(int(command[1]))
        print(int(command[1]))
    elif command[0]=='front':
        if empty(queue)==1:
            print(-1)
        else:
            print(queue[0])
    elif command[0]=='size':
        print(len(queue))
    elif command[0]=='back':
        if empty(queue)==1:
            print(-1)
        else:
            print(queue[-1])
    elif command[0]=='pop':
        if empty(queue)==1:
            print(-1)
        else:
            k = queue.popleft()
            print(k)
    else:
        k=empty(queue)
        print(k)
            
        
        