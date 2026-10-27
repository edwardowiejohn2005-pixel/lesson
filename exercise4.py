def count_even(numbers):
    count = 0

    for h in range(len(numbers)):
        if numbers[h] % 2 == 0:
            count = count + 1

    return count


print(count_even([1, 2, 3, 4, 6, 10]))
print(count_even([1, 3, 5, 7]))
print(count_even([]))