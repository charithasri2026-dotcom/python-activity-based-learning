
# Manufacturing Cost and Profitability Analysis

product = input("Enter product name: ")
units = int(input("Enter number of units produced: "))

if units <= 0:
    print("Invalid number of units")

else:
    material = float(input("Enter raw material cost per unit: Rs. "))
    labor = float(input("Enter labor cost per unit: Rs. "))
    other = float(input("Enter other expenses: Rs. "))
    selling_price = float(input("Enter selling price per unit: Rs. "))

    if material < 0 or labor < 0 or other < 0 or selling_price < 0:
        print("Invalid cost or selling price")

    else:
        total_material = material * units
        total_labor = labor * units

        total_cost = total_material + total_labor + other
        cost_per_unit = total_cost / units
        revenue = selling_price * units
        profit = revenue - total_cost

        print("\nProduct Name:", product)
        print("Total Manufacturing Cost: Rs.", round(total_cost, 2))
        print("Cost Per Unit: Rs.", round(cost_per_unit, 2))
        print("Total Revenue: Rs.", round(revenue, 2))

        if profit > 0:
            print("Profit: Rs.", round(profit, 2))
        elif profit < 0:
            print("Loss: Rs.", round(abs(profit), 2))
        else:
            print("No Profit No Loss")

