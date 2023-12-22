weight = 150  # Replace with actual weight in pounds
height = 67  # Replace with actual height in inches

bmi = weight * 703 / height**2

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 25:
    print("Optimal weight")
else:
    print("Overweight")
