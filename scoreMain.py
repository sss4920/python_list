'''
ScoreMain.py
score.txt 파일에서 한 줄을 읽어 하나의 Score 객체를 만든다.
파일에 저장되어 있는 모든 데이터에 대해 Score 객체를 만들고, 이를 list에 저장한다.
list에 저장된 객체를 출력한다.
'''
import score
text = open(r"C:\temp\score.txt","r")
list=[]
sum=0
for file in text:
    file = file.strip()
    parts=file.split(",")
    s= score.Score(parts[0],int(parts[1]),int(parts[2]))
    list.append(s)
text.close()

mid_avg=0
for s in list:
    s.print()
    print()
    mid_avg+=s.getmid()
print("중간고사 평균: %.2f"%(mid_avg/len(list)))


