def find(array):
    for entry in array:
        if isinstance(entry, int) is False:
            array.remove(entry)

    for entry in array:
        if array.count(entry) > 1:
            array.remove(entry)

    if len(array) < 3:
        return None

    array.sort()

    return array[-2]
