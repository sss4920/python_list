'''
사용자로부터 점수를 입력받아, 이를 리스트에 저장하고 평균을 출력하라
점수의 끝은 음수로 확인한다.
'''
li1=[]
sum=0
while True:
    a = int(input("점수:"))
    if li1  and a<0:
        print("입력된 정수가 없습니다.")
        break
    if a<0 and li1 != None:
        for x in li1:
            sum+=x
        print("입력된 정수:",li1)
        print("점수의 평균은 %.2f입니다."%(sum/len(li1)))
        break
    elif a>=0:
        li1.append(a)



