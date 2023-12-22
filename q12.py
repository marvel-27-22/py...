weight = float(input("Enter the weight of the package in pounds: "))

if weight <= 2:
    rate_per_pound = 1.10
elif weight <= 6:
    rate_per_pound = 2.20
elif weight <= 10:
    rate_per_pound = 3.70
else:
    rate_per_pound = 3.80

shipping_charges = weight * rate_per_pound

print("Shipping charges: $", format(shipping_charges, ".2f"))
