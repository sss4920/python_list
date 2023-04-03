import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
dx =[1,1,0,-1,-1,-1,0,1]
dy =[0,1,1,1,0,-1,-1,-1]
count =0
def dfs(graph,x,y):
    for i in range(8):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<len(graph[0]) and 0<=ny<len(graph):
            if not visit[ny][nx]:
                visit[ny][nx]=1
                if graph[ny][nx]:
                    dfs(graph,nx,ny)
                
                
                    
            
        


while True:
    graph=[]
    col, row = map(int,input().split())
    if not col and not row:
        break
    visit =[[0]*col for _ in range(row)]
    for y in range(row):
        graph.append(list(map(int,input().split())))
    for y in range(row):
        for x in range(col):
            if not visit[y][x] and graph[y][x]:
                
                visit[y][x]=1
                dfs(graph,x,y)
                count += 1
    print(count)
    count=0
