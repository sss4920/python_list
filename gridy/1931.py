n = int(input())
li=[]
for x in range(n):
    li.append(list(map(int,input().split())))
li.sort(key=lambda x:x[0])
li.sort(key=lambda x:x[1])

count=1
end = li[0][1]
for i in range(1,len(li)):
    if li[i][0]>=end:
        count +=1
        end = li[i][1]
print(count)    

            
    
    
    
    