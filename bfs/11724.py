from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,m = map(int,input().split())
li=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int,input().split()))
    li[a].append(b)
    li[b].append(a)
queue = deque([])
visit=[0] * (n+1)
sol = 0

def bfs(n):
    queue = deque(li[n])
    while queue:
        temp=queue.popleft()
        if not visit[temp]:
            visit[temp]=1
            bfs(temp)
        
    



for y in range(1,len(li)):
    if not visit[y]:
        visit[y]=1
        bfs(y)
        sol+=1
print(sol)
                
                