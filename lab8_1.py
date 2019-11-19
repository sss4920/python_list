'''
주제:클래스 정의
작성일: 2019.11.19
'''

class Counter:
    '''
    개수를 세는 클래스
    '''
    def reset(self):
        '''
        count를 0으로 reset
        :return: 없음
        '''
        self.count = 0
    def inc(self,i=1):
        '''
        count를 하나 증가
        :return: 없음
        '''
        self.count +=i
    def current(self):
        '''
        현재 값을 반환
        :return: 현재값
        '''
        return self.count


a = Counter()#생성자를 호출하여 Counter 객체 생성하여 변수 a에 저장
a.reset() #a가 self가 되어 메쏘드 reset이 호출된다.
#reset()의 매개변수를 따로 보낼 필요없어 왜냐면 a가 저절로 self로 전달되니까
a.inc(1) #a를 증가시키기 위해 inc()메쏘드를 호출한다
        #i값을 전달한다.

a.inc(2)
print("a의 현재값은",a.current())