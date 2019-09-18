"""
사용자로부터 x좌표와 y좌표를 입력받아, 원점으로부터의 거리를 출력한다.
"""
from math import *
a = int(input("x좌표:"))
b = int(input("y좌표:"))
distance = sqrt(a*a + b*b)
print("원점까지의 거리",distance)
