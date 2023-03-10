n = int(input())
count=[i for i in range(n+1)]
count[1]=0
# 0,0,2,3,4,5..
for x in range(2,n+1):
    count[x]=count[x-1]+1
    
    if x%3==0 and count[x]>count[x//3]+1:
        count[x]=count[x//3]+1
    if x%2==0 and count[x]>count[x//2]+1:
        count[x]=count[x//2]+1
print(count[n])
    
    