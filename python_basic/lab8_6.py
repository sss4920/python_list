'''
좌표평면에서 점을 나타내는 point 클래스를 정의한다
x,y좌표를 받는 생성자
문자열을 반환하는 __str__
두 점 사이의 거리를 반환하는 getDistance
x축의 대칭점을 반환하는 getXsymmetry
y축의 대칭점을 반환하는 getYsymmetry
원점의 대칭점을 반환하는 getOriginSymmetry 메소드를 정의한다

프로그램에서
p1(3,5),p2(-2,5) 두 점을 정의한다.
p1,x축대칭, y축대칭, 원점대칭점 출력
p1과 p2의 거리를 출력한다.
'''
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y= y
    def getDistance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    def getXsymmetery(self):
        return Point(self.x,(-1*self.y))
    def getYsymmetery(self):
        return Point(self.x*(-1),self.y)
    def getOriginSymmetry(self):
        return Point(self.x*(-1),self.y*(-1))
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
p1=Point(3,5)
p2=Point(-2,5)
print("p1과 p2사이의 거리:",p1.getDistance(p2))
print("p1의 좌표:",p1)
print("p1의 x축 대칭점:",p1.getXsymmetery())
print("p1의 y축 대칭점:",p1.getYsymmetery())
print("p1의 원점 대칭점:",p1.getOriginSymmetry())