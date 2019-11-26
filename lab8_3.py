'''
원 클래스를 정의하라
반지름을  private instance variable로 설정한다
반지름을 매개변수로 받는 생성자를 정의한다 반지름이 0보다 작은 값이 들어오면 0으로 설정한다
setRadius, getRadius 메쏘드를 정의한다.
넓이를 반환하는 getArea 메쏘드를 정의한다.
원의 반지름을 출력하는  print메쏘드를 정의한다.
'''
class Circle:
    PI=3.14# 클래스 변수로 어느메쏘드에서도 속하지않는다. 클래스 내에서 유일
    def __init__(self,r):
        self.__radius=r     #setter를 부르는 것도 가능하다.
    def setRadius(self,r):
        if r<0:
            self.__radius=0
        else:
            self.__radius=r
    def getRadius(self):
        return self.__radius
    def getArea(self):
        return (self.__radius**2)*Circle.PI
    def getLength(self):
        return self.__radius*2*Circle.PI
    def print(self):
        print("반지름 %d인 원입니다."%self.__radius)
    def getPI():
        return Circle.PI
    def setPi(p):
        Circle.PI=p

dong = Circle(4)
print("PI: ", Circle.getPI())
Circle.setPi(3.1415)
print("원의 넓이는 ",dong.getArea())
print("원의 둘레: ",dong.getLength())
dong.setRadius(-5)
dong.print()


