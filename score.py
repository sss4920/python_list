'''
score.py
Score 클래스를 정의한다.
__init__ 함수에서는 이름, 중간고사, 기말고사 성적을 저장한다
__str__ 함수는 Score 객체의 값을 문자열로 변환하여 반환한다. (csv 형식)


'''
class Score:
    def __init__(self,name,mid,fin):
        self.name = name
        self.mid=mid
        self.fin=fin
    def __str__(self):
        return str(self.name)+","+str(self.mid)+","+str(self.fin)
    def print(self):
        print("이름:%s\n중간고사: %s\n기말고사: %s\n"%(self.name,self.mid,self.fin))
    def getmid(self):
        return self.mid
