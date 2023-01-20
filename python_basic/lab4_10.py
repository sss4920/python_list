"""
2단부터 9단까지 구구단을 출력하라
출력예)
2단
2 * 1 =2
...
3단
3*1 = 3
...
"""
for x in range(2,10):
    print("%d단"%x)
    for y in range(1,10):
        print("%d * %d = %d"%(x,y,x*y))
