# the range
for number in range(1, 11, 3):
    print(number)

sum = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum += number

print(sum)

# calculate the sum of all even numbers from 1 to 100 including 1 and 100
sum  =0
for number in range(2, 101, 2):
        sum += number

print(sum)
