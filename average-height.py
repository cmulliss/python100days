# student_heights = [180, 124, 165, 173, 189, 169, 146]
# 180 124 165 173 189 169 146
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# print(sum(student_heights))
# print(len(student_heights))

# thesum = sum(student_heights)
# avg = int(thesum) / len(student_heights)
# print(round(avg))

# using for loops instead of len and sum

total_height = 0
for height in student_heights:
    total_height += int(height)
print(total_height)

no_of_students = 0
for student in student_heights:
    no_of_students += 1

average_height = total_height / no_of_students
print(round(average_height))
