# Polymorphism  - ability to take many shapes (way to use a class exactly like its parent but still each child class keeps its own methods as they are)
from _03_Inheritance import swe1, des1


def motivate_employees(employees: list):
    for employee in employees:
        employee.salary += 300


motivate_employees([swe1, des1])

print(swe1.salary)
print(des1.salary)
