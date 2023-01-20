"""
sqaure 함수는 제곱을 반환하는 함수이다. 이를 정의하라
프로그램에서 1부터 5까지 정수에 대해 squre함수를 호출하여 제곱을 반환받은 후 아래와 같이 출력한다

"""
def square(x):
    return x**2
print("정수","제곱")
for x in range(1,6):
    print(x,"",square(x))


