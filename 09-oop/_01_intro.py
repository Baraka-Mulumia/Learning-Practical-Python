from ast import alias


item1 = "Phone"
item1_price = 100
item1_quantity = 5
item1_price_total = item1_quantity * item1_price


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        print("I am CREATED")

    def calculate_total_price(self):
        return self.price * self.quantity


phone = Item("Phone", 100, 5)

total_price = phone.calculate_total_price()
print(total_price)


class SoftwareEngineer:

    # class attribute - belongs to the class
    alias = "Keyboard Magician"

    # Instance attribute
    def __init__(self, name, age, level, salary) -> None:
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


swe1 = SoftwareEngineer("Baraka", 23, "Junior", 30_000)
swe2 = SoftwareEngineer("Lisa", 22, "Senior", 60_000)

print(swe1.salary)
print(swe1.alias)
print(SoftwareEngineer.alias)
print(swe2.alias)

"""
Create a class ("Blue print")
Create an instance ("Object")
class vs instance 
instance attributes defined in __init__(self)
class attributes
"""
