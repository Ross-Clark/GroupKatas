def problem_1(list_in):
    ordered = sorted(list_in)

    for index, x in enumerate(ordered):
        if index == 0:
            if x == ordered[index + 1]:
                continue
            return x
        if index == len(ordered) - 1:
            return x
        if x != ordered[index + 1] and x != ordered[index - 1]:
            return x


def problem_2(list_in):
    ordered = sorted(list_in)
    for index, x in enumerate(ordered):
        if index == len(ordered) - 1:
            return False
        if x == ordered[index + 1]:
            return True
