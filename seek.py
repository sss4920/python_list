infile = open("text.txt", "r+")

str = infile.read(20)
print("읽은 문자열:",str)
position = infile.tell()
print("현재위치:", position)

position = infile.seek(0,1)
str = infile.read(20)
print("다시읽은 문자열:",str)
infile.close()