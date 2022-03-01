# Base class

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} working ........")

# child class


class SoftwareEngineer(Employee):

    role = "Engineer"

    # inheritance
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)

        self.level = level

    # override functionality

    def work(self):
        print(f"{self.name} is writing code")

    # Child classes can have their own methods
    def codeWith(self, language):
        print(f"{self.name} is coding in {language}")


class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing")

    def draw(self, tool):
        print(f"{self.name} is drawing in {tool}")


swe1 = SoftwareEngineer("Baraka", 23, 3000, "Junior")
swe1.work()
swe1.codeWith("PYTHON")

des1 = Designer("Gorge", 23, 4000)
des1.work()
des1.draw("adobe illustrator")
