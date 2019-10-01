"""
문제: 1에서 100까지 1씩 증가하면서 반복하고 홀수의 합을 구하라
"""
s = 0
for i in range(1,101,1):
    if i % 2 == 0:
        continue
    else:
        s = s+1

print("100까지 홀수의 합",s)