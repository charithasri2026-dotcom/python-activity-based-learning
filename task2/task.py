
# Progressive Electricity Billing

name = input("Enter consumer name: ")
units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 2
    print("Consumer Name:", name)
    print("Electricity Bill: Rs.", bill)
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
    print("Consumer Name:", name)
    print("Electricity Bill: Rs.", bill)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
    print("Consumer Name:", name)
    print("Electricity Bill: Rs.", bill)

