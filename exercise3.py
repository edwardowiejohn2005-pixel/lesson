def list_sum(numbers):
    total = 0

    for p in range(len(numbers)):
        total = total + numbers[p]

    return total


print(list_sum([2, 4, 6, 8, 10]))
print(list_sum([-5, 10, -2]))
print(list_sum([]))