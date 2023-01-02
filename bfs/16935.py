from collections import deque
a, b = map(int,input().split())
queue=deque([])
queue.append([a,1])

exiit=True

while queue:
    temp = queue.popleft()
    if temp[0]==b:
        exiit=temp[1]
        break
    if temp[0]>b:
        exiit=-1
        continue
    else:
        queue.append([int(str(temp[0])+"1"),temp[1]+1])
        queue.append([temp[0]*2,temp[1]+1])
    
print(exiit)
