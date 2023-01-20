'''
import 하지말고 deepcopy 함수를 정의하라
261페이지에 있는 프로그램을 import 하지말고 작동시켜라
'''
def deepcopy(li):
    li2=list(li)
    return li2
scores = [10,20,30,40,50]
values = deepcopy(scores)
print(scores)
print(values)