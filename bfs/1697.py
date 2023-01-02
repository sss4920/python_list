from collections import deque
from collections import deque
queue = deque([])
N,K = map(int,input().split())
visited=[0]*100001
queue.append([N,0])
while queue:
    temp = queue.popleft()
    visited[temp[0]]=1
    if temp[0]<0:
        continue
    if temp[0]==K:
        print(temp[1])
        break
    
    if temp[0]+1<100001 and not visited[temp[0]+1]:
        queue.append([temp[0]+1,temp[1]+1])
    if not visited[temp[0]-1] and temp[0]-1>=0:
        queue.append([temp[0]-1,temp[1]+1])
    if temp[0]*2<100001 and not visited[temp[0]*2]:
        queue.append([temp[0]*2,temp[1]+1])
    
        
    
    
    
    

