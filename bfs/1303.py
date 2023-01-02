row,col = map(int,input().split())
graph=[]
for x in range(col):
    graph.append(list(input()[:]))
visit=[[0]*row for _ in range(col)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

count=0
result1=0
result2=0
def dfs(x,y,condition):
    global count
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<row and 0<=ny<col:
            if not visit[ny][nx]:
                if condition==graph[ny][nx]:
                    visit[ny][nx]=1
                    count+=1
                    dfs(nx,ny,condition)
for y in range(col):
    for x in range(row):
        if not visit[y][x]:
            visit[y][x]=1
            count+=1
            dfs(x,y,graph[y][x])
            if graph[y][x]=='W':
                result1+=count**2
            else:
                result2+=count**2
            count=0
print(result1,result2)
                    
                        
    