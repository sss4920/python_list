'''
복소수를 나타내는 클래스 complex를 정의한다 두실수를 매개변수로 받아 복소수를 정의하는 생성자를 정의한다.
실수부를 반환하는 getrealpart
허수부를 반환하는 getimagepart
복소수의 문자열을 반환하는 __str__ 를 정의한다.
켤레복소수를 반환하는 pair
두 수의 합을 반환하는 __add__
두 수의 곱을 반환하는 __mul__

'''
class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i= i
    def getRealPart(self):
        return self.r
    def getImagePart(self):
        return self.i
    def __str__(self):
        if self.i>=0:
            return str(self.r)+'+'+str(self.i)+'i'
        else:
            return str(self.r)+str(self.i)+'i'
    def pair(self):
        return Complex(self.r, -1*(self.i))
    def __add__(self, other):
        return Complex((self.r+other.r),(self.i+other.i))
    def __mul__(self, other):
        return Complex((self.r*other.r-self.i*other.i),(self.r*other.i+self.i*other.r))
c1 = Complex(3.5,4.6)
c2= Complex(5.4,-7.2)
print(c1)
print(c2)
print(c1.pair())
print(c1+c2)
print(c1*c2)