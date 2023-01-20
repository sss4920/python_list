a = input().split(" ") # a[0] = 횟수 a[1] = 크기
b = input().split(" ") # 입력받은 수들
a = list(map(int,a))
b = list(map(int,b))
li = []
i = 0
for x in b:
    if x < a[1]:
        li.append(x)
li = list(map(int,li))
for a in li:
    print(li[i],end=" ")
    i+=1
