"""
문제:
사용자로부터 3개의 영어단어를 입력받는다
각 단어의 2번째 알파벳을 뽑아서 새로운 문자열을 만든후
이를 출력하라
예)
첫번재 단어:age
두번째 단어:school
세번째 단어: university
출력 예)
gcn
"""
a = input("첫번째 단어: ")   #첫째단어를 받아 a에 저장
b = input("두번째 단어: ")   #위와 동일
c = input("세번째 단어: ")   #위와동일
print(a[1]+b[1]+c[1])   # 문자열의 두번째들을 모아 더해서 출력