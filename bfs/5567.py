from collections import deque
queue=deque([])
N = int(input())
graph=[[] for _ in range(N+1)]
visit = [0]*(N+1)
friendship=int(input())
for x in range(friendship):
    temp=list(map(int,input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])
for x in graph[1]:
    visit[x]=1
    queue.append([x,1])
while queue:
    temp = queue.popleft()
    if not visit[temp[0]] and temp[1]==2:
        visit[temp[0]]=1
        continue
    elif temp[1]>2:
        continue
    else:
        for y in graph[temp[0]]:
            queue.append([y,temp[1]+1])

for x in visit[2:]:
    visit[0]+=x
print(visit[0])
            
        
        
        
        
    

    
    