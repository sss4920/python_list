import sys
input = sys.stdin.readline


def union(array,a,b):
    left = find(array, a)
    right = find(array, b)
    if left>right:
        array[left]=right
    else:
        array[right]=left
        
        

def find(array, a):
    if a==array[a]:
        return a
    return find(array,array[a])

def cycle(array, a, b):
    if find(array, a)==find(array, b):
        return True
    return False



computer = int(input())
line = int(input())

array = [] #이거는 그냥 케이스의 배열이고
family = [ i for i in range(computer+1)]

for x in range(line):
    temp = list(map(int,input().split()))
    array.append(temp)
array.sort(key = lambda x : x[2])
sum=0

for temp in array:
    if not cycle(family, temp[0],temp[1]):
        union(family,temp[0],temp[1])
        sum+=temp[2]
print(sum)