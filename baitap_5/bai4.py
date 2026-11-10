def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
numbers = [5, 10, 65, 20]
result = calculate_sum(numbers)
print(result) 