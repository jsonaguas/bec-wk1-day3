#Task 1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

failed = [i for i in grades if i < 80]
index = grades.index(failed[0])
student = students[index]
grade = grades[index]
activity = activities[index]
print(student, grade, activity)


#Task 2 & Task 3
students_approved = [i for i in students if i != "Jane"]
print(students_approved)
