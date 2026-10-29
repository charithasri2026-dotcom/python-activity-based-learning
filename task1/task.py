
# University Scholarship Allocation

name = input("Enter student name: ")
marks = float(input("Enter marks percentage: "))
income = float(input("Enter annual family income: "))

if marks >= 80 and income <= 200000:
    print(name, "is Eligible for Scholarship")
else:
    print(name, "is Not Eligible for Scholarship")

