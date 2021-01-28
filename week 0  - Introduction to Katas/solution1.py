def findSingleNumber(input):
    for i in input:
        if input.count(i) == 1:
            return i
