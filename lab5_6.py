"""
삼각형의 넓이를 구하는 함수 tri_area를 정의한다 밑변 w와 높이 h를 매개변수로 받아서 넓이를 반환한다

프로그램에서 사용자로부터 밑변과 높이를 입력받아서, 넓이를 출력하라
tri_area를 호출할 때 키워드 인수를 사용한다
입력예)
밑변:5
높이:10
출력예)
삼각형의 넓이:25
"""
under = int(input("밑변:"))
height = int(input("높이:"))
def tri_area(w,h):
    return (w*h)/2
print("넓이:%.2f"%tri_area(w=under,h=height))