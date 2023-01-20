'''
직사각형의 가로(w),세로(h)가 멤버 애트리뷰트다
init(i,j) #가로가 i 세로가 j로 초기화
area() 넓이를 반환
length 둘레를 반환
print() 가로와 세로를 출력 (예) 가로 3 세로 5인 직사각형입니다.)
프로그램에서는
새로운 직사각형 객체를 생성하여 가로 3 세로 5로 설정하고
메쏘드를 이용하여 가로 세로 출력, 넓이 출력 둘레를 출력하라
'''
class Rectangle:

    def init(self,i,j):
        self.w=i
        self.h=j
    def area(self):
        return self.w*self.h
    def length(self):
        return self.w*2+self.h*2
    def print(self):
        print("가로 %d 세로 %d 인 직사각형입니다."%(self.w,self.h))
nemo = Rectangle() # Rectangle 클래스의 객체를 생성하여 변수 r에 저장
nemo.init(3,5) # 3과 5로 초기화 시켜부려
nemo.print()# 메소드 프린트 실행
print("둘레",nemo.length())#둘레의 길이 츨력
print("넓이",nemo.area())# 넓이 길이 출력 nemo의 member로 뚝딱뚝딱한 값 출력
