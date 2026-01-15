numbers = [2, 4, 13, 67, 84, 93]

even_numbers = tuple(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)