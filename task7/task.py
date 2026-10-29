
# Retail Billing with Multiple Discount Rules

name = input("Enter customer name: ")
amount = float(input("Enter purchase amount: Rs. "))

if amount < 0:
    print("Invalid purchase amount")

else:
    if amount >= 5000:
        discount_rate = 0.20
    elif amount >= 2000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount = amount * discount_rate
    discounted_amount = amount - discount

    if amount >= 5000:
        member_discount = discounted_amount * 0.05
    else:
        member_discount = 0

    total_discount = discount + member_discount
    final_bill = amount - total_discount

    print("\nCustomer Name:", name)
    print("Original Amount: Rs.", round(amount, 2))
    print("Discount Amount: Rs.", round(total_discount, 2))
    print("Final Bill: Rs.", round(final_bill, 2))

