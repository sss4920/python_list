'''
영화 제목과 평점을 저장하는 클래스 Movie를 정의한다.
__init__은 영화 제목과 평점을 매개변수로 받아 초기화한다.
getTitle()은 영화 제목을 반환한다
getScore()는 평점을 반환한다
__ str__는 영화제목과 평점을 보기좋게 문자열로 만들어 반환한다
print()는  영화제목과 평점을 출력한다

'''
class Movie():
    def __init__(self,title,score):
        self.title = title
        self.score =score
    def getTitle(self):
        return self.title
    def getScore(self):
        return self.score
    def __str__(self):
        return "영화제목:"+self.title+"평점은:"+self.score
    def print(self):
        print(self.title,self.score)
