pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

total_cents = pennies + nickels * 5 + dimes * 10 + quarters * 25

if total_cents == 100:
    print("Congratulations! You win the game!")
else:
    
    if total_cents > 100:
        print("The amount entered is more than one dollar.")
    else:
        print("The amount entered is less than one dollar.")
