'''import random

number = random.randint(1,100)

a = int(input())
'''
"""
가위바위보를 사용자가 이길때까지 반복하기
"""
import random



while (True):
    com = random.randint(1, 3)
    user = int(input("1. 가위 2.바위 3.보\n"))
    if com == 1: # 컴이 가위면
        if user == 1: # 내가 가위면
            print("가위입니다.비겼습니다!")
            print("다시시도하세요")
        elif user ==2:  # 내가 바위면
            print("바위입니다. 이겼습니다!")
            print("축하합니다.")
            break
        else:
            print("보입니다. 졌습니다.")    #내가 보면
            print("다시시도하세요")
    elif com == 2: # 컴이 바위면
        if user == 1:# 내가 가위면
            print("가위입니다.졌습니다!")
            print("다시시도하세요")
        elif user == 2:# 내가 바위면
            print("비겼습니다")
            print("다시시도하세요")
        else:#내가보면
            print("바위입니다. 이겼습니다!")
            print("축하합니다.")
            break
    else: # 컴이 보면
        if user == 1:#내가 가위면
            print("가위입니다.이겼습니다!")
            print("축하합니다.")
            break
        elif user == 2:#내가 바위면
            print("바위입니다. 졌습니다!")
            print("다시시도하세요")
        else:#내가 보면
            print("보입니다. 비겼습니다.")
            print("다시시도하세요")


