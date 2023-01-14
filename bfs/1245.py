import sys
sys.setrecursionlimit(10**6)
row,col = map(int,input().split())
visit=[[0]*col for _ in range(row)]
graph=[]
for i in range(row):
    temp=list(map(int,input().split()))
    graph.append(temp)
dx=[1,1,0,-1,-1,-1,0,1]
dy=[0,1,1,1,0,-1,-1,-1]
mount=0
def dfs(x,y):
    global is_top
    visit[y][x]=1
    for i in range(8):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<col and 0<=ny<row:
            if graph[ny][nx]>graph[y][x]:
                is_top=False
            if not visit[ny][nx]:     
                if graph[ny][nx]==graph[y][x]:
                    dfs(nx,ny)
is_top=True
for y in range(row):
    for x in range(col):
        if not visit[y][x]:
            if graph[y][x]>0:
                is_top=True
                dfs(x,y)
                
                if is_top:
                    mount+=1
print(mount)