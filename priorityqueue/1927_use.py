import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = [] # heapq에 넣을 heap 만들기
for _ in range(n):
    temp = int(input())
    if temp==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,temp)
        

