"""
문제: 사용자로부터 정수를 입력받아서, 1부터 해당 정수까지 출력한다.
print_int 함수를 먼저 정의하고 정수를 매개변수로 받아서 1부터 해당 매개변수값까지 출력하는 함수다.
"""
def print_int(a):
    """
    :param a: 매개변수a
    :return: 없음
    """
    for x in range(1,a+1):
        print(x,end=" ")
a = int(input("정수를 입력하세요:"))
print_int(a)

