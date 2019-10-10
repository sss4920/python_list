"""
문제: sum_list는 두개의 매개변수를 받는다.첫 번째 매개변수는 리스트이고 두번째 매개변수는 start로서 어디부터 합할 지를 의미한다
start의 두번째 매개변수는 default값으로 0을 가진다 예를 들어 sum_list(ㅣ,2)는 2번째 요소부터 시작하여 리스트의 합을 구하여 반환한다
sum_list(l)은 0번째 요소부터 시작하여 리스트의 합을 구하여 반환한다.
"""
def sum_list(a,b=0):
    """
    :param a:리스트
    :param b:start 인덱스
    :return:sum총합
    """
    sum = 0
    for x in range(b,len(a)):
        sum+=a[x]
    return sum

l= [-5,4,6,10,3]
print("sum_list(l,2)=",sum_list(l,2))
print("sum_list(l)=",sum_list(l))
