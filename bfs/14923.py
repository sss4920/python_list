
row,col=map(int,input().split())
start_x,start_y=map(int,input().split())
end_x,end_y=map(int,input().split())
graph=[ [] for _ in range(row)]
visit_temp=[ [0]*col for _ in range(row)]
wall_visit=[ [0]*col for _ in range(row)]
visit_zero=[ [0]*col for _ in range(row)]
for y in range(row):
    temp = list(map(int,input().split()))
    graph[y]=temp
dx = [1,0,-1,0]
dy = [0,1,0,-1]
count=[0,10000]

def bfs(x,y):
    print(x,y)
    if x==end_x-1 and y==end_y-1:
        print(visit_temp)
        if count[0]<count[1]:
            count[1]=count[0]
        return
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<col and 0<=ny<row:
            if visit_zero[ny][nx]==1 and visit_temp[y][x]+1<visit_temp[ny][nx] and graph[ny][nx]==0:
                visit_temp[ny][nx]=visit_temp[y][x]+1
            if not visit_zero[ny][nx] and graph[ny][nx]==0:
                visit_zero[ny][nx]=1
                visit_temp[ny][nx]=visit_temp[y][x]+1
                bfs(nx,ny)
            
                
                
for y in range(row):
    for x in range(col):
        if graph[y][x] and not wall_visit[y][x]:
            graph[y][x]=0
            wall_visit[y][x]=1
            visit_temp[start_y-1][start_x-1]=1
            visit_zero=[ [0]*col for _ in range(row)]
            bfs(start_x-1,start_y-1)
            print(count[0])
            graph[y][x]=1
            visit_temp=wall_visit
            count[0]=0
        

    
        