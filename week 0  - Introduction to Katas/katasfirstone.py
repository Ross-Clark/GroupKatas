def kata1(list):
    for i in list:
        count = list.count(i)
        if count==1:
            return i