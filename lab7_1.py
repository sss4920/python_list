'''
튜플을 매개변수로 받아서 해당 튜플에 있는 최소값과 최대값을 반환하는 mmin_max함수를 정의하라
ㅠㅡ로그램에서는 5개의 정수값을 가지는 튜플을 정의하고  min_max 함수를 호출하여 결과를 출력
'''
def min_max(a):
    maxi=a[0]
    mini=a[0]
    for x in a:
        if x>maxi:
            maxi=x
        if x<mini:
            mini=x
    return mini,maxi
li=(1,2,3,4,5)
mini,maxi=min_max(li)
print("최소값:",mini)
print("최대값:",maxi)
