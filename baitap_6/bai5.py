def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cut_down_list = remove_odd_numbers(original_list)
    print("Original list:", original_list)
    print("Cut-down list:", cut_down_list)