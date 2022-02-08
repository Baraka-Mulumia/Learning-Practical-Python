# add
import weakref


print(3 + 5)

# sub
print(7 - 4)

# mul
print(3 * 2)

# division
print(6/3)

# exponential
print(2**4)

# floor division
print(10//6)


# PEMDAS
print(3 * (3 + 3) / 3 - 3)

# exercise  d-2.2  BMI Calculator (weight devidded by height squared)
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height**2)

print(int(bmi))
