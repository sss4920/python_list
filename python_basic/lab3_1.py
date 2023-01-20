"""
문제: 점수를 입력받아서 60점 이상이면 합격
이하면 불합격을 출력하라
"""
score = int(input("점수:"))
if score >= 60 : # 반드시 콜론을 써줍니다.
    print("합격입니당")  # indentation 들여쓰기 중요 비슷한게 c에서의 중괄호 블럭
    print("아앜")
elif score <60 :
    print("불합격")
    print("재수 ㅊㅊ")
else:
    print("불합격입니당")