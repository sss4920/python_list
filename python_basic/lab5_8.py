"""
매개변수로 넘어온 리스트에서 최소값과 최대값을 반환하는 함수 min_max를 정의한다
프로그램에서
ㅣ=[3,5,-2,20,9]를 정의한 후 , min_max를 호출하여 최소값은 m1최대값은 m2에 저장하고 이를 출력하라

"""
def min_max(l):
    """
    :param l: 리스트
    :return: 최소값,최대값
    """
    min1=l[0]
    max1=l[0]
    for x in l:
        if min1>x:
            min1=x
        if max1<x:
            max1=x
    return min1,max1
l=[3,5,-2,20,9]
m1,m2=min_max(l)
print("최소값:%d"%m1)
print("최대값:%d"%m2)
