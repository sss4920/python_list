'''
person 클래스의 객체 p1을 생성한다. (김일수, 21세)
나이를 한살 올린다.
p1을 출력한다.
'''
from person import *
from student import Student
p1 = Person("김일수",21)
p1.getOlder()
print(p1)
#부모가 자식꺼 못씀

s1 = Student(12345, "김이수", 20)
s1.getOlder()
print(s1)
s1.getSNO()