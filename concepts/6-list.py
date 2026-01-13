marks = [95, 75, 84, 88, 98, 68]

print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])

marks[0] = 87
print(marks[0])
print("################################")

numbers = [3, 6, 9, 2, 5]
numbers .append(4)
numbers.sort()
print(numbers .append(7)) #it return NONE
print(numbers.sort()) #it return NONE
print(numbers)

numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)

fruits = ["banana", "orange", "apple"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)

fruits.insert(1, "mango")
print(fruits)

fruits.remove("mango") #remove first occurence of mango from the list
print(fruits)
fruits.pop(2) #remove the 2nd index value from the list
print(fruits)