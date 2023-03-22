#나름 힙 구현을 머리속으로 해서 해봤는데 시간초과가 뜬다.. 어디가 잘못된 걸까

import sys
input = sys.stdin.readline


n = int(input())
array = [0]
for _ in range(n):
    temp = int(input())
    if temp==0:
        if len(array)==1:
            print(0)
        else:
            print(array[1])
            k = array.pop()
            if len(array)>1:
                array[1]=k
                i = 1
            while i*2+1<len(array):
                if i*2<len(array) and array[i]>array[i*2]:
                    array[i], array[i*2] = array[i*2],array[i]
                    i=i*2
                if i*2+1<len(array) and array[i]>array[i*2+1]:
                    array[i], array[i*2+1] = array[i*2+1],array[i]
                    i=i*2+1
                 
                
    else:
        array.append(temp)
        i = len(array)-1
        while i>=2:
            if array[i//2]>array[i]: #자식이 더 작으면
                k=array[i//2]
                array[i//2]=array[i]
                array[i]=k
            i=i//2
                    
    