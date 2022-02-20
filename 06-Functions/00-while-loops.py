print("start")

i = 0

while i < 10:
    print(i)
    i += 1

print("done")

secrete_number = 78
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: \n"))
    guess_count += 1
    if guess == secrete_number:
        print("You won")
        break
else:
    print("Sorry you failed")
