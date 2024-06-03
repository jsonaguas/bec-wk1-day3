#Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print(sorted_grades)

#Task 2
grades_total = sum(grades) 
grades_count = len(grades) 
score_average = grades_total / grades_count
print(score_average)

#Task 3
failed_grades = ['Failed' if i < 80 else i for i in grades]
print(failed_grades)