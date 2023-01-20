"""
유클리드 호제법을 이용해서 최대공약수와 최소 공배수를 구해라
"""
a,b=map(int,input().split())
maxi = max(a,b)
mini = min(a,b)
while (True):
    if mini == 0:
        break
    r = maxi % mini
    maxi = mini
    mini = r
print("최대공약수:%d"%maxi)
print("최소공배수:%d"%(a*b/maxi))
