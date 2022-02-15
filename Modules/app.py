import random


print(random.randint(1, 100))
print(random.random())

states = ["Nairobi", "Mombasa", "Nakuru"]

# access an item at the beginning
print(states[0])

# access an item at the end
print(states[-1])

# add 1  item at the end of a list
states.append("Kisumu")

# add more than 1 item at the end of a list
states.extend(["Murang'a", "Laikipia"])
print(states)

# get part of an array
print(states[0:4])

