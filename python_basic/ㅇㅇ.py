test=int(input())
for x in range(test):
    a,b=input().split()
    a=int(a)
    temp=''
    for y in b:
        temp+=y*a
    print(temp)

