length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

area1 = length1 * width1

length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

area2 = length2 * width2

if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("The rectangles have the same area.")
