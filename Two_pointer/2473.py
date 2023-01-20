import sys
n=int(input())
fluid=list(map(int,input().split()))
fluid.sort()
min=sys.maxsize
min_list=[]
res=False

for x in range(len(fluid)):
    left=x+1
    right=n-1
    if res:
        break
    while left<right:
        temp=fluid[x]+fluid[left]+fluid[right]
        if temp==0:
            min_list=[fluid[x],fluid[left],fluid[right]]
            res=True
            break
        if min > abs(temp):
            min=abs(temp)
            min_list=[fluid[x],fluid[left],fluid[right]]
        
        if temp<0:
            left+=1
        else:
            right-=1
min_list.sort()
print(*min_list)    
        
        
    
    