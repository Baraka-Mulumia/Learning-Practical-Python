print("Welcome to the tip calculator ")

bill = float(input("What was the total bill ? $ "))
tip_rate = int(
    input("What percentage tip would you like to give? 10, 12 or 15 ? "))

num_of_people = int(input("How many people to split the bill  "))

total_tip = bill * (tip_rate/100)

total_bill = bill + total_tip

bill_per_person = round(total_bill/num_of_people, 2)

print(f"Each person should pay {bill_per_person}")
