'''
한 변의 길이가 50이하인 직각 삼각형의 세변의 길이를 출력하라
[3,4,5]
[5,12,13]
[6,8,10]
...
'''
'''
for x in range(1,51):
    for y in range(x,51):
        for z in range(y,51):
            if (x**2)+(y**2) == (z**2):
                temp.append([x,y,z])
'''


temp=[[x,y,z] for x in range(1,51) for y in range(x,51) for z in range(y,51) if (x**2)+(y**2)==(z**2)]
for x in temp:
    print(x)
