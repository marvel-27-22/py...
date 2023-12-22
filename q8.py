primary_color1 = input("Enter the name of the first primary color: ").lower()
primary_color2 = input("Enter the name of the second primary color: ").lower()

if primary_color1 == "red" and primary_color2 == "blue":
    print("Mixing", primary_color1, "and", primary_color2, "gives you purple!")
elif primary_color1 == "red" and primary_color2 == "yellow":
    print("Mixing", primary_color1, "and", primary_color2, "gives you orange!")
elif primary_color1 == "blue" and primary_color2 == "yellow":
    print("Mixing", primary_color1, "and", primary_color2, "gives you green!")
else:
    print("Invalid primary colors")
