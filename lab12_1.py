'''
주제: 텍스트파일 입출력
일시 : 2019.2.5
'''
infile = open(r"C:\temp\phones.txt","r")
for line in infile:
    line = line.rstrip()
    print(line)
# s = infile.readline()  # iinfile에서 10개의 문자를 문자열로 읽어들여서 s에 배정
# print(s) #문자열을 출력
infile.close() #파일처리가 끝났으므로 closs
