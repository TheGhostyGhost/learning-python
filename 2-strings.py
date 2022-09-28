msg = "Hello World"
print(msg)
print(msg[0])
print(msg[0:5])
print(msg[5:])
print(msg.lower())
print(msg.upper())
print(msg.count("Hello"))
print(msg.count("l"))
msg = msg.replace("World", "Universe")
print(msg.count("Universe"))

greeting = "Hello"
name = "Ghosty"
msg = greeting +", "+ name + ". Welcome!"
print(msg)

msg = "{}, {}. Welcome!" .format(greeting, name)
print(msg)

msg = f"{greeting}, {name}. Welcome!"
print(msg)

# Show an overview of string methods
print(dir(name))

# Gives us more information about string methods
print(help(str.lower))