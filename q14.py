seconds = int(input("Enter the number of seconds: "))

if seconds >= 86400:
    days = seconds // 86400
    seconds %= 86400
    print(f"{days} days")

if seconds >= 3600:
    hours = seconds // 3600
    seconds %= 3600
    print(f"{hours} hours")

if seconds >= 60:
    minutes = seconds // 60
    seconds %= 60
    print(f"{minutes} minutes")

if seconds > 0:
    print(f"{seconds} seconds")
