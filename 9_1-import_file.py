import 9_0-my_module as mm # module is in the same directory so import is successfully

'courses = ["History", "Math", "Physics", "CompSci"]

index = my_module.find_index(courses, "Physics") # full name of module
print(index)

index = mm.find_index(courses, "Physics") # short name of module
print(index)'

# import the function from the module itself
from 9_0-my_module import find_index,  # test is out of the function so it has to be included separately

courses = ["History", "Math", "Physics", "CompSci"]
index = find_index(courses, "Physics")