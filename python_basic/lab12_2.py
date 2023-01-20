file1 = input("원본파일이름:")
file2 = input("복사본 이름:")

infile = open(file1, "rb")
outfile = open(file2, "wb")

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
print(file1+"를"+file2  +"로 복사함")