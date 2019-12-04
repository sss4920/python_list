'''
계좌를 하나 만들어 100원을 입금한 후 10원을 출금. 츨력
0원 적금계좌를 하나 만들어 10000원을 입금한 후 출력. 적금 해약금을 출력
'''

import account
import installAccount

a1 = account.Account('1111','수현',100)
a1.withdraw(10)
a1.print()

a2 = installAccount.installAccount('2222','수현',10000,'12/1')
a2.input(10000)
a2.print()
print("적금 해약금은 : ",a2.close())
