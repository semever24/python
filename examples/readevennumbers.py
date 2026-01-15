data = open("numbers.txt","r")
read_data = data.read()
data.close()

numbers = read_data.split(",")
numbers = [int(num) for num in numbers]
count = 0

for i in numbers:
    if(i%2 == 0):
        count+=1

print("List of numbers in file: ", read_data)
print("Total even numbers in count: ", count)        