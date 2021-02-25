def determine(anagram, input):

    if len(anagram) != len(input):
        return False

    for char in input:
        if input.count(char) != anagram.count(char):
            return False

    return True
