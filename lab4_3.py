"""
사용자로부터 자연수를 입력받아서, factorial 값을 출력하라.
입력예)
자연수:3
출력예)
3!=6
"""
"""
fac = int(input("자연수:"))
fact = 1
for x in range(1,fac+1):
    fact *= x
print("%d!=%d"%(fac,fact))
"""
"""
# while문을 사용
i = int(input("수 입력:")) # 입력받기
s = 0 # 합은 반드시 초기화 필요
j = 2 # 짝수를 나타내는 변수
while (j<i):
    s += j
    j += 2
# 반복 끝, 출력
print("%d보다 작은 짝수의 합: %d"%(i,s))
"""
fac = int(input("자연수:"))
fact = 1
i=1
while(i<=fac):
    fact *= i
    i+=1
print("%d!=%d"%(fac,fact))
