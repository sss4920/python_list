import sys
from collections import deque

input = sys.stdin.readline

dy = [-2,-1,1,2,2,1,-1,-2]
dx = [1,2,2,1,-1,-2,-2,-1]

    



test = int(input())
for _ in range(test):
    width = int(input())
    x, y  = map(int,input().split())
    goal_x,goal_y = map(int,input().split())
    queue = deque([])
    queue.append([x,y,0])
    visit = [[0]*width for _ in range(width)]
    visit[y][x]=1
    while queue:
        temp = queue.popleft()
        if temp[0]==goal_x and temp[1]==goal_y:
            print(temp[2])
            break
        for i in range(8):
            nx = temp[0]+dx[i]
            ny = temp[1]+dy[i]
            if 0<=nx<width and 0<=ny<width:
                if not visit[ny][nx]:
                    visit[ny][nx]=1
                    queue.append([nx,ny,temp[2]+1])
            
                    
                
            
     

