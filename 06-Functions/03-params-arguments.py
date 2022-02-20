# Create a function called describe_me()
# Write 3 print statements that describe yourself inside the function
# Call the greet function and run your code

from ast import arguments


def describe_me():
    print("Hi, I am baraka mulumia")
    print("A peer counselor for reforming addicts")
    print("I can swim, dance and ride horses")


# describe_me()

# Dynamic functions
# Having functions that allow inputs

# positional arguments
def greet(name):
    print(f"Hello {name}")


greet("Joyland")
greet("Billie")


def sum(a, b):
    print(f"{a} + {b} = {a+ b}")


# named (keyword ) arguments
sum(b=10, a=30)


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with(location="Oxford", name="Baraka")
