base_fare = float(input("Enter base fare: "))
distance = float(input("Enter distance (km):"))
total = base_fare + distance * 12.5

is_discounted = input(("senior citizen or pwd? (y/n)") == "y

if is_discounted:
    total *= 0.80
    print("total fare is ", total)
else:
    print("total fare is ", total)