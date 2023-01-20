"""
정수의 각 자리수의 합을 출력하라.
입력예)
정수:546
출력예)
자리수의 합:15
"""
num = int(input("정수:"))
i=1
sum=0
while (0<num):
    sum += num % 10
    num = num//10
print("자리수의 합:",sum)
