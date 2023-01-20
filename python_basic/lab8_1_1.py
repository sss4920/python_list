'''
Counter 클래스에 dec 메쏘드를 추가하시오 매개변수가 넘어오지 않으면 1을 감소시키고
변수가 있다면 매개변수 값 만큼 감소시킨다. 단, counter 값은 최소 0이다.
프로그램에서 dec를 매개변수 없이 호출한후 Counter 값을 출력
 dec의 매개변수를 100으로 호출한 후 Counter 값을 출력
'''

class Counter:
    def __init__(self,i=0): #생성자 메쏘드 특별한 메쏘드ㅏ
        self.count=i
    def dec(self,i=1):
        self.count-=i
        if self.count<0:
            self.count=0
a = Counter(5)
a.dec()
print(a.count)
a.dec(100)
print(a.count)