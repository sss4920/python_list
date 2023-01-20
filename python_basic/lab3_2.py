"""
매장에서 주문가능한 메뉴를 리스트로 정의한다 햄버거,샌드위치.클라,사이다
이를 화면에 출력한다
사용자로부터 메뉴의 번호(0~3)을 입력받고, 갯수를 입력 받아서 선택된 메뉴와 총 가격을 출력한다
각 메뉴의 가격은 햄버거는 3천원으로 샌드위치 2000원 콜라 사이다는 천원
"""

list = ["햄버거", "샌드위치", "콜라","사이다"]
print(list)
number = int(input("메뉴의 번호:"))
yang = int(input("몇개:"))
if number == 0:
    sum = yang * 3000
if number == 1:
    sum = yang * 2000
else :
    sum = yang * 1000
print("선택된 메뉴:",list[number])
print("총가격:",sum)