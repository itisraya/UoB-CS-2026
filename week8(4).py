a = int(input("Enter your number: "))

if a !=0  and a% 11 ==0 and a %5 == 0:
    print("The number is divisible by 11 and 5")
elif a !=0 and a % 11 == 0:
    print("The number is divisible by 11")
elif a !=0 and a % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 11 and 5")
