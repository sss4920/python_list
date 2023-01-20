'''
계좌 정보를 저장하는 Account 클래스를 정의한다
계좌번호, 계좌주이름, 잔액을 저장하는 __init__함수
input은 입금액을 잔액에 추가
withdraw는 출금액을 잔액에서 차감
print  함수는 현재 계좌정보를 출력
'''
class Account:
    def __init__(self,anumber,name,mymoney):
        self.anumber=anumber
        self.name = name
        self.mymoney = mymoney
    def input(self,money):
        self.mymoney+=money
    def withdraw(self,money):
        self.mymoney-=money
    def print(self):
        print("나의 잔액은:",self.mymoney)
