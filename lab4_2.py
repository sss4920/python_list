"""
사용자가 입력하는 수보다 작은 짝수의 합을 구하라
입력예) 수입력:8
출력예) 8보다 작은 짝수의 합: 12
"""
num = int(input("수입력:"))
sum = 0
for x in range(2,num,2):
    if (x<=num) & (x % 2) == 0:
        sum += x
print("%d보다 작은 짝수의 합:"%num,sum)
