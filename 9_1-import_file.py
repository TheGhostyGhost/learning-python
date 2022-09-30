import my_module as mm # module is in the same directory so import is successfully

courses = ["History", "Math", "Physics", "CompSci"]

index = my_module.find_index(courses, "Physics") # full name of module
print(index)

index = mm.find_index(courses, "Physics") # short name of module
print(index)

# import the function from the module itself
from my_module import find_index, test  # test is out of the function so it has to be included separately

courses = ["History", "Math", "Physics", "CompSci"]
index = find_index(courses, "Physics")
print(index)
from my_module import *  # import everything from module with (*)

courses = ["History", "Math", "Physics", "CompSci"]
index = find_index(courses, "Physics")
print(index)

# module not in directory add new path for python to look for modules/functions
import sys
sys.path.append("C:\\Users\\Geisti\\Documents\\Workspace\\learning-python\\modules")

from my_module_2 import find_index_2, test
index_2 = find_index_2(courses, "Physics")
print(index_2)
