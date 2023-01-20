"""
두 수를 매개변수로 받아, 두 수중 작은 수를 반환하는 min함수를 정의한다.
"""
def min(a,b):
    small = 0
    if a>b:
        small = b
    else:
        small=a
    return small
k,g = input("두 수:").split()
k=int(k)
g=int(g)
print("작은 수",min(k,g))
