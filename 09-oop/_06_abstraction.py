# Abstraction  = each object should only expose a high level mechanism of using it and hide internal implementation details
# Encapsulation  -Hiding of data implementation

class SoftwareEngineer:

    # class attribute - belongs to the class
    alias = "Keyboard Magician"

    # Instance attribute
    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level
        # Internal attribute
        self.__salary = None
        self.__num_of_bugs_solved = 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        # hr does not care about the inner workings of calc salary
        self.__salary = self.__calculate_salary(value)

    @salary.deleter
    def salary(self):
        del self.salary

    # private functions
    def solve_bug(self):
        self.__num_of_bugs_solved += 1

    def __calculate_salary(self, base_value):
        if self.__num_of_bugs_solved < 10:
            return base_value
        if self.__num_of_bugs_solved < 100:
            return base_value * 1.5
        return base_value * 1.75


swe1 = SoftwareEngineer("Baraka", 23, "Junior")
swe2 = SoftwareEngineer("Lisa", 22, "Senior")

print(swe1.name)
print(swe1.age)


for i in range(90):
    swe1.solve_bug()


swe1.salary = 6000
print(swe1.salary)
