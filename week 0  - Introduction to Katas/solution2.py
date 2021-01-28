def findDuplicates(input):
    for i in input:
        if input.count(i) == 2:
            return True
        else:
            continue
    return False