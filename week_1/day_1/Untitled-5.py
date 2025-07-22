user_number=input("enter a number between 1 and 100:")
user_number=int(user_number)
if user_number % 3:
    print("Fizz")
elif user_number % 5:
    print("Buzz")
elif user_number % 3 and user_number % 5:
    print("FizzBuzz")


