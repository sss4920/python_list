'''
이름: 전화번호를 가지는 딕셔너리를 생성하여 5개의 원소로 초기화하고
이름을 입력하면 해당 전화번호를 출력하고
해당이름이 없다면 전화번호가 없습니다를 출력
마지막에 전체의 이름과 전화번호를 출력
'''
dic = {"김수현":"1111","ㅇㅇ":"2222","ㄱㄱ":"3333","ㄴㄴ":"4444","ㄷㄷ":"5555"}
name = input("이름:")
if name in dic.keys():
    print("%s 전화번호는 %s"%(name,dic[name]))
else:
    print("해당 전화번호가 없습니다.")
for x in dic:
    print(x,dic[x])
