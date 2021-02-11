from typing import List


def second_smallest(input_list: List):
    remove_chars = [i for i in input_list if isinstance(i, int)]
    sorted_list = sorted(remove_chars, reverse=True)
    return sorted_list[-2] if sorted_list[-1] != sorted_list[-2] else None
