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

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):

        self.__salary = self.__calculate_salary(value)

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
swe1.set_salary(5000)
print(swe1.get_salary())


for i in range(90):
    swe1.solve_bug()


swe1.set_salary(5000)
print(swe1.get_salary())
