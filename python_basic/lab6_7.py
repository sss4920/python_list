'''
C:\temp\data.txt 파일에 한 줄에 하나씩 과일 이름을 5개 넣는다.
사용자로부터 과일 이름을 입력받아서 해당 과일이  data.txt파일에 있는 과일이면, "재고가 있습니다"없는과일이면 "제고가 없습니다"출력

'''
data=[]
f = open("C:\Temp\data.txt","r",encoding='utf-8-sig')
a=input()
flag = False
for line in f.readlines():
    if a in line:
        flag=True
        break
    else:
        flag = False
if flag:
    print("재고가 있습니다.")
else:
    print("재고가 없습니다.")

