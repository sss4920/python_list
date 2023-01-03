from collections import deque
f,s,g,u,d = list(map(int,input().split()))
queue=deque([])
queue.append([s,0])
visit=[0]*(f+1)
dx=[u,-d]
ans="use the stairs"
if g==s:
    queue.popleft()
    ans=0
else:
    visit[s]=1
while queue:
    temp=queue.popleft()
    x=temp[0]
    level=temp[1]
    if x==g:
        ans=level
        break
    for i in range(2):
        nx=x+dx[i]
        if 1<=nx<f+1:
            if not visit[nx]:
                visit[nx]=1
                queue.append([nx,level+1])
print(ans)