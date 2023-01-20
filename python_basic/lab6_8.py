'''
각 층별로 3호실로 구성되어 있는 4층짜리 연립주택이 있다고 가정하자.
각 층의 호실별로 전기사용량을 배정하고 (임의의 값으로 채운다.)
각 층별 전기사용량의 합계,최고값,최저값
전체 세대 전기사용량의 합계,최고값,최저값을 구하라.
이차원 배열을 이용한다.
(출력)
1층 최고: 345 최저 242 합: 10223
2층
3층
4층
전체 최고:848 최저: 10 합:123242
'''
hotel = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
realmax=[]
realmin=[]
realsum=0
for x in range(len(hotel)):
    max=hotel[x][0]
    min=hotel[x][0]
    sum=0
    for y in (hotel[x]):
        if max<=y:
            max=y
        if min>=y:
            min=y
        sum+=y
        realsum+=y
    print("%d층 최고: %d 최저: %d 합: %d"%(x+1,max,min,sum))
    realmax.append(max)
    realmin.append(min)
maxi=realmax[0]
mini=realmin[0]
for x in realmax:
    if x>maxi:
        maxi=x
for x in realmin:
    if x<mini:
        mini=x
print("전체 최고: %d 최저: %d 합:%d"%(maxi,mini,realsum))


