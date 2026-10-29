
# Railway Fare and Reservation Calculator

name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
distance = float(input("Enter distance in km: "))

print("Classes: Sleeper, AC3, AC2")
travel_class = input("Enter travel class: ").lower()

if age < 0 or distance <= 0:
    print("Invalid input")

elif travel_class not in ["sleeper", "ac3", "ac2"]:
    print("Invalid travel class")

else:
    if travel_class == "sleeper":
        fare = distance * 1.5
    elif travel_class == "ac3":
        fare = distance * 2.5
    else:
        fare = distance * 3.5

    if age < 5:
        fare = 0
    elif age >= 60:
        fare = fare * 0.80

    print("\nPassenger Name:", name)
    print("Age:", age)
    print("Distance:", distance, "km")
    print("Travel Class:", travel_class.upper())
    print("Final Ticket Fare: Rs.", round(fare, 2))

