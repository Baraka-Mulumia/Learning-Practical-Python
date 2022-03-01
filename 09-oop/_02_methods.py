class SoftwareEngineer:

    # class attribute - belongs to the class
    alias = "Keyboard Magician"

    # Instance attribute
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # Instance methods
    def code(self):
        print(f"{self.name} is writting code")

    def codeWith(self, language):
        print(f"{self.name} is writting code in {language}")

    def information(self):
        information = f"name = {{self.name}} age = {{self.age}}  level ={{self.level}}"
        print(information)

    # D_UNDER Methods - you can override inbuilt methods
    def __str__(self):
        information = f"name = {{self.name}} age = {{self.age}}  level ={{self.level}}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    #  Class Methods - no self
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


swe1 = SoftwareEngineer("Baraka", 23, "Junior", 3000)
swe2 = SoftwareEngineer("Lisa", 22, "Senior", 6000)

swe1.code()
swe2.codeWith(language="PYTHON")
swe2.information()
print(swe2 == swe1)
print(SoftwareEngineer.entry_salary(45))
