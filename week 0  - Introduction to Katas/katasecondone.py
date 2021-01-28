def kata2(list):
    for i in list:
        count = list.count(i)
        if count==2:
            return True