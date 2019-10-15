"""
람다함수를 이용하여 절대값을 출력하라.
l=[-3,2,1]

"""
L = (lambda x:-x if x<0 else x)
l=[-3,2,1]
for f in l:
    print(L(f))