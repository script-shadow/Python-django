# 2.Gym memberships are priced based on age: $25 for adults (18 and over), $15 for children. Everyone gets a $5 discount on januarry
age = int(input("Enter your age: "))
month = input("Enter the month 1-12: ")

match month:
    case "1":
        month="january"
    case "2":
        month="february"
    case "3":   
        month="march"
    case "4":
        month="april"
    case "5":
        month="may"
    case "6":
        
        month="june"
    case "7":
        month="july"
    case "8":
        month="august"
    case "9":
        month="september"
    case "10":
        month="october"
    case "11":
        month="november"
    case "12":
        month="december"
    case _:
        print("Invalid month number. Please enter a number between 1 and 12.")
if month == "january":
    if age >= 18:
        price = 25 - 5
        print(f"Your gym membership price is: ${price}")
    else:
        price = 15 - 5
        print(f"Your gym membership price is: ${price}")
else:
    if age >= 18:
        price = 25
        print(f"Your gym membership price is: ${price}")
    else:
        price = 15
        print(f"Your gym membership price is: ${price}")