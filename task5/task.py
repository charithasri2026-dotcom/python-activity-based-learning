
# Multi-Plan Telecommunications Cost Optimization

name = input("Enter customer name: ")
minutes = float(input("Enter monthly call minutes: "))
data = float(input("Enter monthly data usage in GB: "))

if minutes < 0 or data < 0:
    print("Invalid input")
else:
    basic = 199 + (minutes * 1) + (data * 10)
    standard = 399 + (minutes * 0.50) + (data * 5)
    premium = 599

    print("\nCustomer Name:", name)
    print("Basic Plan Cost: Rs.", round(basic, 2))
    print("Standard Plan Cost: Rs.", round(standard, 2))
    print("Premium Plan Cost: Rs.", round(premium, 2))

    if basic <= standard and basic <= premium:
        cheapest = "Basic Plan"
        cost = basic
    elif standard <= basic and standard <= premium:
        cheapest = "Standard Plan"
        cost = standard
    else:
        cheapest = "Premium Plan"
        cost = premium

    print("Cheapest Plan:", cheapest)
    print("Monthly Cost: Rs.", round(cost, 2))

