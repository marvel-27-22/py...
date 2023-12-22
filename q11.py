
packages_purchased = int(input("Enter the number of packages purchased: "))

if packages_purchased >= 100:
    discount = 0.50
elif packages_purchased >= 50:
    discount = 0.40
elif packages_purchased >= 20:
    discount = 0.30
elif packages_purchased >= 10:
    discount = 0.20
else:
    discount = 0  # No discount for less than 10 packages
discount_amount = discount * 99 * packages_purchased
total_cost = (1 - discount) * 99 * packages_purchased

print("Discount amount: $", format(discount_amount, ".2f"))
print("Total cost: $", format(total_cost, ".2f"))
