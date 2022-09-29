# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is
# and
# or
# not

language = "Python"

if language == "Python":
    print("Language is Python")
elif language == "Java": # elif can be used for switch-cases statements
    print("Language is Java")
elif language == "R":
    print("Language is R")
else:
    print("No match")^

# Boolean




user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# or
if user == "Admin" or logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# not
if not logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# difference between == and is
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b) # false because they are two different objects in memory
print(id(a))
print(id(b))
b = a # assign memory (id) of a to b
print(id(a))
print(id(b))
print(a is b)
print(a == b)

# False Values:
    # False
    # None
    # Zero of any numeric
    # Any empty sequence. For example: "", (), []
    # Any empty mapping. For example: {}

condition = False

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
condition = None
condition = False
condition = False