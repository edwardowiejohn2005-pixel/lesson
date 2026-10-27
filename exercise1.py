def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


print(find_largest([3, 46, 56, 100, 76, 9]))
print(find_largest([-10, -5, -2, -18]))
print(find_largest([]))