
# Examination Result and Grace-Mark Validation

name = input("Enter student name: ")

marks = []
for i in range(1, 4):
    score = int(input(f"Enter marks for subject {i}: "))
    marks.append(score)

if any(score < 0 or score > 100 for score in marks):
    print("Invalid marks. Enter marks between 0 and 100.")

else:
    failed = [i for i in range(3) if marks[i] < 40]

    if len(failed) == 1:
        i = failed[0]

        if 35 <= marks[i] <= 39:
            marks[i] = min(marks[i] + 5, 40)

    total = sum(marks)
    percentage = total / 3

    print("\nStudent Name:", name)
    print("Final Subject Marks:", marks)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")

    if all(score >= 40 for score in marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")

