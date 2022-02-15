fruits = ["apple", "mango"]

states_of_kenya = ["Mombasa", "Nairobi", "Nakuru", "Delaware", "Pennsylvania"]

# accessing items positive
print(states_of_kenya[0])

# accessing items negative
print(states_of_kenya[-1])

# mutate an item in the list
states_of_kenya[2] = 'NaxVegas'

# add at the end
states_of_kenya.append("Kisumu")

# add at the begining
states_of_kenya.extend(["Kilifi", "Muran'ga", "Jesus"])

print(states_of_kenya)
