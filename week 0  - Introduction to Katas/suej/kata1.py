def kata_1(numbers):
    for number in numbers:
        if numbers.count(number) == 1:
            return number

