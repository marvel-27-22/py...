age = int(input("Enter the person's age: "))

if age <= 1:
    print("The person is an infant.")
elif age <= 12:
    print("The person is a child.")
elif age <= 19:
    print("The person is a teenager.")
else:
    print("The person is an adult.")
