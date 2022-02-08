# use the round function
print(round(2.6666666666666, 2))

# floor division
result = 4 / 2

result += 10

print(f"the result of 4 / 2 + 10 = {result}")

# d-2.3 life in weeks exercise

age = input("What is your current age? \n")
num_age = int(age)

num_of_years_left = 90 - num_age
num_of_days_left = num_of_years_left * 365
num_of_months_left = round(num_of_years_left * 12)
num_of_weeks_left = round(num_of_years_left * 52)


result = f"You have {num_of_days_left} days left, {num_of_weeks_left} weeks left, {num_of_months_left} months left"

print(result)
