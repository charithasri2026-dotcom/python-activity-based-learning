
# Campus Event Financial Planning

event = input("Enter event name: ")
participants = int(input("Enter number of participants: "))

if participants < 0:
    print("Invalid number of participants")
else:
    registration_fee = float(input("Enter registration fee per participant: Rs. "))
    venue_cost = float(input("Enter venue cost: Rs. "))
    food_cost = float(input("Enter food cost per participant: Rs. "))
    other_expenses = float(input("Enter other expenses: Rs. "))

    if (registration_fee < 0 or venue_cost < 0
            or food_cost < 0 or other_expenses < 0):
        print("Invalid expense or fee")

    else:
        revenue = participants * registration_fee
        total_food_cost = participants * food_cost
        total_expenses = venue_cost + total_food_cost + other_expenses
        profit = revenue - total_expenses

        print("\nEvent Name:", event)
        print("Total Revenue: Rs.", round(revenue, 2))
        print("Total Food Cost: Rs.", round(total_food_cost, 2))
        print("Total Expenses: Rs.", round(total_expenses, 2))

        if profit > 0:
            print("Event Profit: Rs.", round(profit, 2))
        elif profit < 0:
            print("Event Loss: Rs.", round(abs(profit), 2))
        else:
            print("Event Break-even: No Profit, No Loss")

