user_number=int(input("enter a number between 1 and 100:"))
if user_number % 3==0 and user_number % 5==0:
    print("Fizzbuzz")
elif user_number % 3==0:
    print("fizz")
elif user_number % 3 and user_number % 5==0:
    print("Buzz")


else:
    print("The number is not divisible by 3 or 5")