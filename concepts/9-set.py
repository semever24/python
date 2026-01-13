set_values = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4}

print(set_values)
print(type(set_values))

empty_dictionary = {}
print(empty_dictionary)
print(type(empty_dictionary))

empty_set = set()  # syntax for empty set
print(empty_set)
print(type(empty_set))

set_values.add("hello")
set_values.add(25)
set_values.add("Python")
set_values.add(189)
print(set_values)

set_values.remove(189)
print(set_values)

set_values.pop()
print(set_values)

set_values.clear()
print(set_values)

print("###########################################")

set1 = {1, 2, 5, 7, "Python", 7, 9, "Hey"}
set2 = {101, 2, 51, 7, "Lab", 17, 91, "Hey"}

print(set1)
print(set2)
print(set1.union(set2)) # union of two sets
print(set1.intersection(set2)) # intersection of two sets means give the common values in both sets (i.e) same values