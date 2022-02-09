print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("Whats your age? "))
bill = 0

if height >= 120:
    print('Can ride')
    if age < 12:
        print("Child Tickets  are $5 ")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7 ")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay have a free ride on us")
    else:
        print("Adult tickets  are  $12 ")
        bill = 12
    wants_photo = input("Do you want a photo takes?  Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride")
