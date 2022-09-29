# Dictionaries are used to store data values in key:value pairs
# A key-value pair consists of two related data elements: 
# 1. key: which is a constant that defines the data set (e.g., gender, color, price)
# 2. value: which is a variable that belongs to the set (e.g., male/female, green, 100)

student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(student)

# update values
student["name"] = "Jane" # updates the name from "John" to "Jane"
student["phone"] = "555-555" # adds a new key = "phone" with value "555-555" to student 
print(student)

# update multiple keys and values with update()
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
student.update({"name": "Jane", "age": 26, "phone": "555-555"})
print(student)

# delete a key - method 1
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
del student("age")

# delete a key - method 2 with pop() / grabs & removes a value
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
age = student.pop("age")
print(student)
print("age")

# how many items in dictionary
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)