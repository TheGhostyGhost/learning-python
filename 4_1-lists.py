from operator import truediv
from textwrap import indent


courses = ["History", "Math", "Physics", "CompSci"]

print(courses[2])
print(courses[:1])
print(courses[2:])

# Insert data to courses
courses.insert(1, "Art")
print(courses)

# List within list
courses_2 = ["History_1_2", "Math_1_2"]
courses.insert(0, courses_2)
print(courses)

# Extend the list with another list
courses = ["History", "Math", "Physics", "CompSci"]
courses.extend(courses_2)
print(courses)

# Remove items from list
courses = ["History", "Math", "Physics", "CompSci"]
courses.remove("Math")
print(courses)

# Remove the last item from list
courses = ["History", "Math", "Physics", "CompSci"]
lastitem = courses.pop()
print(lastitem)

# Reverse list
courses = ["History", "Math", "Physics", "CompSci"]
courses.reverse()
print(courses)

# Sort list methods
courses = ["History", "Math", "Physics", "CompSci"]
courses.sort()
num = [1, 2, 5, 4, 3]
num.sort()
print(courses)
print(num)
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)

# Sorted function
courses = ["History", "Math", "Physics", "CompSci"]
sourted_courses = sorted(courses)
print(sourted_courses)

# min, max, sum
num = [1, 2, 5, 4, 3]
print(min(num))
print(max(num))
print(sum(num))

# index
courses = ["History", "Math", "Physics", "CompSci"]
print(courses.index("History"))
print(courses.index("Physics"))

# check if value is in the list TRUE or FALSE
print("Art" in courses)
print("Math" in courses)

# looping through list and print item
for item in courses:
        print(item)

# looping through list and print item plus index
for item in enumerate(courses):
        print(item)

for index, item in enumerate(courses):
        print(index, item)

for index, item in enumerate(courses, start=1):
        print(index, item)

# turning list into a string with separator
courses = ["History", "Math", "Physics", "CompSci"]
courses_str = ", ".join(courses)
print(courses_str)

# turning string into a list
new_list = courses_str.split(", ")
print(courses_str)
print(new_list)

