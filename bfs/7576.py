from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]
queue=deque([])
wid , col = map(int,input().split())
graph=[]
for x in range(col):
    graph.append(list(map(int,input().split())))
visit=[[-1] * wid for _ in range(col)]
result=0
exit_number=0
for y in range(col):
    for x in range(wid):
        if graph[y][x]==1:
            queue.append([x,y,0])
            visit[y][x]=0
        elif graph[y][x]==-1:
            visit[y][x]=1

while queue:
    temp=queue.popleft()
    for i in range(4):
        nx = dx[i]+temp[0]
        ny = dy[i]+temp[1]
        if 0<=nx<wid and 0<=ny<col:
            if visit[ny][nx]<0:
                visit[ny][nx]=temp[2]+1
                queue.append([nx,ny,temp[2]+1])
for y in range(col):
    for x in range(wid):
        if 0>visit[y][x]:
            exit_number=-1
            break
        elif graph[y][x]==-1:
            continue
        elif visit[y][x]>result:
            result=visit[y][x]

if exit_number==-1:
    print(-1)
else:
    print(result)