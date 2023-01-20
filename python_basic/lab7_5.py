'''
학번과 점수를 dictionary 를 이용하여 5개 정도 정의한다
사용자로부터 학번과 점수를 입력받아 만약 기존에 해당 학번이 없으면 dictionary 에 추가한다
성적이 높은 순으로 출력하라.
'''
a={'201914009':10,'20000000':20,'100000000':30,'342ㅕ49':40,'24234':50}
s = input("학번:")
s1 = int(input("점수:"))
if s not in a:
    a[s]=s1
li=sorted(a,key=a.__getitem__,reverse=True)
for x in li:
    print(x)

