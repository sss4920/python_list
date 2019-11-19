'''
두 명의 사용자로부터 좋아하는 과일을 입력받는다 빈 칸을 띄어서
여러 개 입력받을 수 있다 집합연산을 이용하여 두명이 모두 좋아하는 과일을 출력하라
'''
a=input("a가 좋아하는 과일:").split()
b=input("b가 좋아하는 과일:").split()
a=set(a)
b=set(b)
c=a.intersection(b)
print("a와 b가 좋아하는 과일:",end=" ")
for x in c:
    print(x,end=" ")
