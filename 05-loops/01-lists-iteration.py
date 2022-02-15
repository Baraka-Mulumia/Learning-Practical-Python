students = ["Jim", "Belgin", "Garry", "Edwin", "Larry"]

for student in students:
    print(f'{student}')

# 5.1 avg height exercise
input_heights = input("Input a list of student heights ").split()

student_heights = []

for height in input_heights:
    student_heights.append(float(height))

print(student_heights)

# 5.2 Highest score
student_scores = []

input_scores = input("Input a list of student scores ").split()

for score in input_scores:
    student_scores.append(float(score))

print(student_scores)
