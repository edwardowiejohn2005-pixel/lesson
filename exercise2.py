def find_smallest(numbers):
    if len(numbers) == 0:
        return None

    smallest = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]

    return smallest


print(find_smallest([8, 3, 12, 0, 7]))
print(find_smallest([-3, -10, -1, -6]))
print(find_smallest([]))