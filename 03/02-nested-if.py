print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("Whats your age? "))

if height >= 120:
    print('Can ride')
    if age < 12:
        print("Please pay  $5 ")
    elif age <= 18:
        print("Please pay $7 ")
    else:
        print("Please pay  $12 ")
else:
    print("Sorry you have to grow taller before you can ride")


# exercise 2 - BMI Calc
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# exercise 2 - Leap Year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
