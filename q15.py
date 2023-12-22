pocket_number = int(input("Enter a pocket number (0-36): "))

if pocket_number == 0:
    color = "green"
elif 1 <= pocket_number <= 10:
    color = "red" if pocket_number % 2 == 1 else "black"
elif 11 <= pocket_number <= 18:
    color = "black" if pocket_number % 2 == 1 else "red"
elif 19 <= pocket_number <= 28:
    color = "red" if pocket_number % 2 == 1 else "black"
elif 29 <= pocket_number <= 36:
    color = "black" if pocket_number % 2 == 1 else "red"
else:
    color = "Invalid pocket number"

print("The pocket is", color)
