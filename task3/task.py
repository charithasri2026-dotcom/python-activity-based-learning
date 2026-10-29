
# Hospital Billing and Patient Classification

name = input("Enter patient name: ")
days = int(input("Enter number of days admitted: "))

print("Room Types: General, Semi-Private, Private")
room = input("Enter room type: ").lower()

if days <= 0:
    print("Invalid number of days")

elif room == "general":
    bill = days * 1000

elif room == "semi-private":
    bill = days * 2000

elif room == "private":
    bill = days * 3000

else:
    bill = 0
    print("Invalid room type")

if days > 0 and room in ["general", "semi-private", "private"]:
    if days <= 3:
        category = "Short Stay"
    elif days <= 7:
        category = "Medium Stay"
    else:
        category = "Long Stay"

    print("\nPatient Name:", name)
    print("Patient Classification:", category)
    print("Total Hospital Bill: Rs.", bill)

