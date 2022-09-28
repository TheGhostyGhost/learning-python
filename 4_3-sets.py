# Sets

cs_courses = {"History", "Math", "Physics", "CompSci"}
print(cs_courses)

# Remove duplicates / 2nd Math item is not printed
cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
print(cs_courses)

# membership test / test if a value is part of a set
print("Math" in cs_courses)

# interaction between two sets
cs_courses = {"History", "Math", "Physics", "CompSci", "Sport"}
art_courses = {"History", "Math", "Physics", "CompSci", "Art", "Design"}

# values that are in both sets
print(cs_courses.intersection(art_courses))

# values that is not in art_courses
print(cs_courses.difference(art_courses))

# combine all values of both sets
print(cs_courses.union(art_courses))