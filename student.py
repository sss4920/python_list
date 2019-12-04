'''
클래스 정의연습
2019. 11. 28
Student 클래스를 정의한다.
"""
"""
학생 클래스를 정의하여 점수를 계산
생성자는 학번과 이름을 매개변수로 받아 배정한다.
프로그램에서는 3명의 학생의 학번과 이름을 입력받아 3명의 학생을 생성한 후 이를 리스트에 추가한다.
applyMidTerm 중간고사성적을 입력받아 저장한다
applyFinalTerm 기말고사 성적을 입력받아 저장한다.

"중간고사 성적을 입력하세요"라는 안내문을 출력한다.
3명의 학생에 대해 중간고사 성적을 입력받아 저장한다.
"기말고사 성적을 입력화세요"라는 안내문을 출력한다.
기말고사 성적을 입력받아 저장한다.
getAverage()는 평균점수를 self에 저장한후 이를 반환한다
print()는 학생의 학번 이름 중간고사 성적 기말고사 성적 평균을 출력한다.
'''

import person

class Student(person.Person):
    def __init__(self,id,name,age,mid=0,final=0,avg=0):
        super().__init__(name,age) # 슈퍼클래스에 정의된 init함수를 호출
        self.id = id
        self.mid=mid
        self.final=final
        self.avg=avg
    def applyMidTerm(self,MidTerm):
        self.midterm = MidTerm
    def applyFinalTerm(self,Final):
        self.finalterm=Final
    def getSNO(self):
        return self.id
    def getName(self):
        return self.name
    def getAverage(self):
        self.avg=(self.midterm+self.finalterm)/2
        return self.avg
    def print(self):
        print("학번:", self.getSNO(), "이름:", self.getName(), "중간:", "평균:",
              self.getAverage())
    def __str__(self):
        s= super().__str__()
        s = s+"학번:"+str(self.id) +"\n"
        return s
#프로그램 시작







