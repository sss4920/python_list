'''
사람을 정의하는 Person 클래스는 이름과 나이를 가진다
이름과 나이를 벙하는 __init__메쏘드
getOlder 메소드를 호출하면 나이가 1증가한다
getName,getAge 메쏘드가 있다
__str__메쏘드는 다음 형태의 문자열을 반환한다
이름: 홍길동
나이:20세
'''
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getOlder(self):
        self.age+=1
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def __str__(self):
        return "이름:"+str(self.name)+"\n"+"나이:"+str(self.age)+"세"+"\n"
