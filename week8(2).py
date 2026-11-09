a = int(input("Enter a year:"))

if a %4 == 0 and a % 100 !=0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")


#second problem
a = int(input("How old are you? "))

if a >= 18:
    print(" You are allowed to vote")
else:
    print("You are not allowed to vote")
