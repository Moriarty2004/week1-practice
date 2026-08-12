courses = {
    "Python": 25,
    "Java": 18,
    "SQL": 30,
    "Web": 15
}

print("Available Courses:")
for course, count in courses.items():
    print(course, ":", count)

search_course = input("Enter a course name: ")

if search_course in courses:
    print("Enrollment for", search_course, ":", courses[search_course])
else:
    print("Course not found.")

total_students = sum(courses.values())

top_course = max(courses, key=courses.get)
low_course = min(courses, key=courses.get)

popular_courses = set()
for course, count in courses.items():
    if count > 20:
        popular_courses.add(course)

print("\nSummary")
print("Total Enrollments:", total_students)
print("Course with Highest Enrollment:", top_course)
print("Course with Lowest Enrollment:", low_course)
print("Courses Having More Than 20 Students:", popular_courses)