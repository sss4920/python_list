"""
사용자가 한줄에 입력하는 숫자의 합을 구하여 출력하라 몇 개의 숫자가 입력될 지는 알 수 없다.
"""
# a = map(int,(input().split()))
# sum = 0
# for i in a:
#     sum += i
# print(sum)
a = input().split()
sum = 0
for i in a:
    i = int(i)
    sum += i
print(sum)
