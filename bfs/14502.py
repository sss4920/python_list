from collections import deque
import copy
dy =[0,1,0,-1]
dx = [1,0,-1,0]
virus = deque([])
row,col=map(int, input().split())
graph =[]
for x in range(row):
    graph.append(list(map(int,input().split())))
visit = [[0]*col for _ in range(row)]
print(visit)
count = 0
max_count=0
def dfs(x,y): #바이러스 퍼뜨림
    global count,max_count
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<nx<col and 0<ny<row:
            if graph[ny][nx]==0:
                graph[ny][nx]=2
                max_count=1
                dfs(nx,ny)
                graph[ny][nx]=0
    return max_count
                
def wall(count):
    if count==3:
                   
    copy.deepcopy(graph)
            
        
            
sol=0            

for y in range(row):
    for x in range(col):
        if graph[y][x]==2: #바이러스라면
            virus.append([x,y])
            if wall:
                while virus:
                    temp = virus.popleft()    
                    count_temp = dfs(temp[0],temp[1])
                    print(count_temp)
            if count_temp>sol:
                sol=count_temp
            max_count=0
print(sol)
print(visit)