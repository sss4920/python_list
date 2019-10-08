"""
매개변수로 넘어온 리스트에서 최대값을 반환하는 get_max 함수를 정의한다.
프로그램에서,
ㅣ1 = [],ㅣ2=[] 에서 각자 최대값을 출력하고 두 최대값의 합을 출력하라
"""
def get_sum(a):
    temp = a[0]
    for x in a:
        if x >=temp:
            temp=x
    return temp
l1=[3,5,-2,20,9]
l2=[-4,374,3,1,4,7,-23]
print("l1의 최대값:",get_sum(l1))
print("l2의 최대값:",get_sum(l2))
print("l1과 l2최대값 합:",get_sum(l1)+get_sum(l2))