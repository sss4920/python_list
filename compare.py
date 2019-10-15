def min_max(l):
    """
    :param l: 리스트
    :return: 최소값,최대값
    """
    min1=l[0]
    max1=l[0]
    for x in l:
        if min1>x:
            min1=x
        if max1<x:
            max1=x
    return min1,max1
