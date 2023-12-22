mass = float(input("Enter the object's mass in kilograms: "))

weight = mass / 9.8

if weight > 1000:
    print("The object is too heavy (weight:", weight, "newtons).")
elif weight < 10:
    print("The object is too light (weight:", weight, "newtons).")
else:
    print("The object has a weight of", weight, "newtons.")
