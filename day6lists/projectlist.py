# student mark analyzer
marks = [85, 90, 78, 92, 88]
print("Marks:", marks, "\n")

# Total and average
total_marks = sum(marks)
average_marks = total_marks / len(marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Highest and lowest
highest_marks = max(marks)
lowest_marks = min(marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

# Grade based on average marks
if average_marks >= 90:
    print("Grade: A")
elif average_marks >= 80:
    print("Grade: B")
elif average_marks >= 70:
    print("Grade: C")
elif average_marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

count_above_90 = sum(1 for m in marks if m > 90)
print("Students scoring above 90:", count_above_90)


marks.sort()
print("Sorted Marks:", marks)
