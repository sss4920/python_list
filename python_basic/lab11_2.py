'''
주제: 텍스트 파일에 쓰기 연습
일시: 2019. 12. 5.
'''
import os.path



if os.path.isfile(r"C:\temp\phones2.txt"):
    print("이미존재합니다")
else:
    outfile = open(r"C:\temp\phones2.txt", "w")  # 파일을 쓰기용으로 열기
    s = "김일수 010-5433-3442\n"
    outfile.write(s)
    outfile.write("김삼수 010-3334-4333\n")
    outfile.close()
