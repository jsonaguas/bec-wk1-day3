
#Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find students who attended and submitted the assignment
attended_and_submitted = [i for i in attended if i in submitted]
print(attended_and_submitted)

#Task 2
if submitted == attended:
    print("True")
else:
    print("False")  

#Task 3
#Sorry to recycle code but the code for Task 1 produces the same output for this Task
attended_not_submitted2 = [i for i in attended if i in submitted]
print(attended_not_submitted2)

#In a less direct method, I could remove each student individually
attended.remove("Eve")
attended.remove("Frank")
print(attended)


