"""
팩토리얼 계산과정과 값을 출력하라.
"""
a = int(input("양의 정수:"))
b = " "
sum = 1
for x in range(a,0,-1):
    sum *= x
    if x != 1:
        b+=str(x)+"*"
    else:
        b+=str(x)
print("%d! ="%a,b,"= %d"%sum)
