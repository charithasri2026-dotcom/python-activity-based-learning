# Problem Statement
Develop a Python program to calculate a student's examination result and determine eligibility for grace marks. The program should accept the student's name and marks in three subjects as input. Each subject has a maximum of 100 marks, and the minimum passing mark is 40.

If a student scores between 35 and 39 marks in exactly one subject and scores at least 40 marks in the other two subjects, the student is eligible for 5 grace marks in that subject. The grace marks should be added to the subject score, up to a maximum of 40 marks. The program should display the final marks, total marks, percentage, and result (Pass or Fail).

Note: These are sample rules for the programming assignment, not official examination regulations.
# Algorithm
1. Start.
2. Input the student's name.
3. Input marks in three subjects.
4. Check whether each subject's marks are between 0 and 100.
5. If the marks are invalid, display an error message.
6. Count the number of subjects in which the student scored below 40.
7. If the student failed in exactly one subject and scored between 35 and 39 in it, check whether the other two subjects have at least 40 marks.
8. If eligible, add 5 grace marks to the failed subject, without exceeding 40 marks.
9. Calculate the total marks and percentage.
10. If all three subjects have at least 40 marks after applying grace marks, display Pass; otherwise, display Fail.
11. Display the final subject marks, total marks, percentage, and result.
12. Stop.
# Mermaid Flowchart
```mermaid

flowchart TD
    A([Start]) --> B[/Input student name and 3 subject marks/]
    B --> C{All marks between 0 and 100?}
    C -- No --> D[/Display Invalid Marks/]
    C -- Yes --> E[Find subjects below 40]
    E --> F{Failed in exactly one subject?}
    F -- Yes --> G{Failed subject marks between 35 and 39?}
    G -- Yes --> H{Other two subjects passed?}
    H -- Yes --> I[Add 5 grace marks, maximum 40]
    H -- No --> J[Keep original marks]
    G -- No --> J
    F -- No --> J
    I --> K[Calculate total and percentage]
    J --> K
    K --> L{All subjects have 40 or more?}
    L -- Yes --> M[/Display Pass/]
    L -- No --> N[/Display Fail/]
    M --> O[/Display final marks and percentage/]
    N --> O
    D --> P([Stop])
    O --> P
  ```




# Input Source Code (Python)

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



# Sample Input and Output
Input:
Enter student name: Charitha
Enter marks for subject 1: 65
Enter marks for subject 2: 37
Enter marks for subject 3: 72


Output:
Student Name: Charitha
Final Subject Marks: [65, 40, 72]
Total Marks: 177 / 300
Percentage: 59.0 %
Result: PASS


# Calculation
- Subject 1 = 65 marks
- Subject 2 = 37 + 5 grace marks = 42, capped at 40
- Subject 3 = 72 marks
- Total marks = 65 + 40 + 72 = 177/300
- Percentage = (177 ÷ 300) × 100 = 59%
- Final result = PASS
