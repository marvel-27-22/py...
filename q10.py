
books_purchased = int(input("Enter the number of books you purchased this month: "))

if books_purchased == 0:
    points = 0
elif books_purchased == 1:
    points = 5
elif books_purchased == 2:
    points = 15
elif books_purchased == 3:
    points = 30
else:
    points = 60
    
print("You earned", points, "points this month!")
