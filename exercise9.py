def first_duplicate(numbers):
    seen = set()

    for i in range(len(numbers)):
        if numbers[i] in seen:
            return numbers[i]

        seen.add(numbers[i])

    return None


print(first_duplicate([4, 7, 2, 7, 5, 4]))
print(first_duplicate([1, 2, 3, 4]))
print(first_duplicate([5, 5, 3]))