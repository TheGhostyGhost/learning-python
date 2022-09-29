
def hello_func():
    return "Hello Function"

hello_func() # reuse code without repeating - DRY (don' repeat yourself)
hello_func() # all changes from the function are updated whener the function is called
hello_func()
hello_func()

print((hello_func().upper()))

def hello_func(greeting):
    return "{} Function.".format(greeting) # .format is relevant for the argument {}

print(hello_func("Hi"))

def hello_func(greeting, name = "You"):
    return "{}, {} Function.".format(greeting, name) # .format is relevant for the argument {}

print(hello_func("Hi")) # if no value is entered for name, "You" will be assigned to name
print(hello_func("Hi", "Ghosty"))

# *args - Passing the arguments as a tuple or list. Here the elements In-Order-Of-Appearance are assigned to the arguments of the function.
# **kwargs - Transfer of the arguments as a dictionary. The values are assigned to the arguments of the function via the keys.
def student_info(*args, **kwargs): 
    print(args)
    print(kwargs)

student_info("Math", "Art", name = "John", age = 22)

courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(courses, info)
student_info(*courses, **info)