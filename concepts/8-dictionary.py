data = {
    "name" : "SK",
    "age" : 36,
    "height" : 6.2,
    "location" : "Bangalore",
    "subjects" :  ("maths", "science", "physics"),
    "marks" : [85, 95, 83]
    }

print(data)
print(type(data))
print(data["name"])
print(data["subjects"])
print(data["marks"])

print("########################################")

students = {
    "name" : "SK",
    "subjects" : {
        "maths" : 98,
        "physics" : 85,
        "chemistry" : 83,
        "science" : 95
    }
}

print(students)
print(students["subjects"])
print(students["subjects"] ["physics"], students["subjects"] ["science"])
students.update({"age" : 35, "location" : "Bangalore", "weight" : "91.5kg"})
print(students.keys())
print(list(students.keys()))
print(len(list(students.keys())))
print(students.values())
print(students.items())
print(students.get("age"))