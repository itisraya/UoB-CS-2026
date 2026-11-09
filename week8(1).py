a = float(input("Enter your number: "))

if not a < 0 and 70 < a < 100:
    print("You are first ")
elif 60 < a < 69:
    print("You are 2.1")
elif 50 < a < 59:
    print("You are 2.2")
elif 40 < a < 49:
    print("You are 3rd")
elif 0 < a < 39:
    print("Fail")
else:
    print("Invalid score")


