name = input("Enter student name: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)
total = sum(marks)
average = total / 5
highest = max(marks)
lowest = min(marks)
passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"
above_average = []
for mark in marks:
    if mark > average:
        above_average.append(mark)
print("\nSTUDENT REPORT CARD")
print("Customer Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Subjects Passed:", passed)
print("Subjects Failed:", failed)
print("Final Grade:", grade)
print("Marks Greater than Average:", above_average)