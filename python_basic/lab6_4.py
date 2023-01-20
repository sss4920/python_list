'''
사용자로부터 한줄에 여러 개의 숫자를 입력받는다
입력 받은 숫자들을 역순으로 출력하라
입력 예)
숫자들 입력:5 7 9 10 4 -5 7
출력 예)
역순: 10 9 7 7 5 4 -5

'''
a = list(map(int,input("숫자들 입력:").split()))
b=sorted(a,reverse = True)
sum1=0
print("역순:",b)
for x in b:
    sum1+=x
print("합:%d"%sum1)
