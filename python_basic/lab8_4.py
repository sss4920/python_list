'''
student 클래스를 정의한다. 학번의 최초값은 20000 이다
이름을 매개변수로 받아 학번과 이름을 설정한다. 한 학생이 생성하고 나면 학번은 하나 증가 시켜놓는다.
학생의 정보를 출력하는 print 함수가 있다.(학번,이름)
학생의 수를 반환하는 클래스 메쏘드 getCount가 있다.

프로그램에서 세명의 학생을 생성하고, 학생의 정보를 출력한다.
학생의 수를 getCount 함수를 호출하여 출력한다.
'''
class student:
    sum=0
    def __init__(self,name,id=20000):
        self.__name=name
        self.__id = student.sum+id
        student.sum += 1
        student.getCount()
    def getCount():
        return student.sum

    def print(self):
        print("학번:",self.__id,"이름",self.__name)
a = student("a")
b=student("b")
c=student("c")
a.print()
b.print()
c.print()
print(student.getCount())




