friends = 1


def increase_friends():
    global friends
    friends += 1
    print(f"Friends inside function {friends}")


increase_friends()
print(f"Friends outside a function {friends}")


def add(a): return a * 5


def increase_friends_2():
    return friends + 1


friends = increase_friends_2()
