'''
적금계좌 정보를 저장하는 install어쩌구 클래스는 Account 클래스를 계승한다
계좌번호 ,계좌주 이름, 잔액, 적금일을 저장하는 __init__함수
적금을 해약하는 close 함수가 있다 현재 잔액에 2%이율을 계산하여 반환한다.
'''
import account
class installAccount(account.Account):
    def __init__(self,anumber,name,mymoney,date):
        super().__init__(anumber,name,mymoney)
        self.date=date
    def close(self):
        return self.mymoney*0.02