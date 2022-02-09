print("Welcome to love calculator")

your_name = input("What is your name? \n")
partners_name = input("What your partners name \n")

your_names = your_name + partners_name

combined_name = your_names.lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

true = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

print(f"{love_score}%")

if love_score > 90 or love_score < 10:
    print(
        f"Your score is {love_score}%, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}% you are alright together")
else:
    print(f'Your score is {love_score}% ')
