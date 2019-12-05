'''
사용자로부터 이름과 전화번호를 입력받아서, phones.txt파일에 추가하라 lab12_1을 실행하여 내용을 확인하라.
한줄에는 한사람의 이름과 전화번호가 표시된다.
'''
outtext = open(r"C:\temp\phones.txt",'a')
outtext.write(input("이름과 전화번호를 쓰세요:"))
outtext.close()
