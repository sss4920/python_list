"""
두수를 입력받아 두 수의 모든 약수 출력하기
"""
a,b = map(int,input().split(" "))
maxi = max(a,b)
mini = min(a,b)
yak = []
yak1 = []
gong = 0
for x in range(maxi+1):
    if a % (x+1) == 0 :
        yak.append(x+1)
    if b % (x+1)== 0:
        yak1.append(x+1)
print(yak)
print(yak1)
for x in range(mini+1):
    if (a % (x+1)==0) & (b % (x+1)==0):
        gong = x+1
        print("공약수:",x+1)
if gong ==1:
    print("공약수가 없습니다.")
else:
    print("최대공약수 : %d"%gong)

