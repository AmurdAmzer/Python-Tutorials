### We have two types of Functions

# 1. Function that performs a task


def greet(name):
    print(f"Hello {name}")

greet("Ahmed")


# 2. Function that returns a value

def greet(name):
    return f"Hello {name}"

greet("Ahmed")
message = greet("Ahmed")

## The takeaway is, the first type of function only prints the output in the terminal. the second type of functions returns the output, which can be stored (eg. it is stored in message) and can be used later.
