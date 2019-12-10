'''
(movie.txt)영화제목과 평점을 저장한 텍스트파일을 작성한다(ansi로 저장)
예) 제목과 평점은 ,로 구별된다
아이언맨,9.8
겨울왕국2,9.9
감쪽같은 그녀,9.28
나이브스 아웃, 8.88
라스트 크리스마스, 7.77
(movieMain.py)
movie.txt에 저장되어있는 내용을 읽어서 Movie 객체를 만든 후, 이를 movie.p에 binary 형태로 저장해라
'''
import movie
import pickle
file = open("movie.txt","r")
list=[]
for x in file:
    parts = x.split(",")
    line=movie.Movie(parts[0],parts[1])
    pickle.dump(line, open("movie.p","wb"))
    line = pickle.load(open("movie.p","rb"))
    print(line)


