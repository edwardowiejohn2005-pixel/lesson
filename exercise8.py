def has_duplicates(numbers):
    seen = set()

    for i in range(len(numbers)):
        if numbers[i] in seen:
            return True

        seen.add(numbers[i])

    return False


print(has_duplicates([1, 2, 3, 2]))
print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([])) 