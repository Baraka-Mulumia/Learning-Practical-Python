
friends = 1


def increase_friends():
    friends = 2
    print(f"Friends inside function {friends}")


increase_friends()
print(f"Friends outside a function {friends}")


def drink_portion():
    # Variables and functions are locally scoped
    alcohol_content = 45
    print(alcohol_content)


# print(alcohol_content)

# Global scope
height = 5.7


def show_height():
    print(height)


show_height()

# Anything you give a name to has a name space

# there is no block scope in python  (if, while, )

if 3 > 2:
    age = 45

print(age)
