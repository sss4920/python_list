from student import Student


a = Student(id=int(input("학번:")),name=input("이름:"))
b = Student(id=int(input("학번:")),name=input("이름:"))
c = Student(id=int(input("학번:")),name=input("이름:"))
list = []
for x in a,b,c:
    list.append(x)
    x.applyMidTerm(int(input("중간고사 성적을 입력하세요:")))
    x.applyFinalTerm(int(input("기말고사 성적을 입력하세요:")))
for x in a,b,c:
    x.print()