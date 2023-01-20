"""
두수를 입력받아 절댓값이 큰수, 작은수를 출력하라.
max, min 써서 할수도 있다.
"""
a = int(input("첫번째수:"))
b = int(input("두번째수:"))
a=abs(a)
b=abs(b)
if a >b :
    print("절대값이 큰수의 절대값:",a)
    print("절대값이 작은수의 절대값:",b)
else:
    print("절대값이 큰수의 절대값:", b)
    print("절대값이 작은수의 절대값:", a)