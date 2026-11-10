def remove_uneven(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
first = [1, 2, 4, 5, 6, 7, 8]
second = remove_uneven(first)
print(first)
print(second)