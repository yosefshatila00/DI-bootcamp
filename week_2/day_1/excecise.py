def display_message():
    print("i am learning about functions in python")

display_message()


def favorite_book(title):
    print(f"one of my favorite books is {title}")

favorite_book("lions_king")


def discribe_city(city , country="unknown"):
    print(f"{city} is in {country}")

discribe_city("paris", "france")



import random

def pick_num():
    number=int(input("enter a number between 1 and 100\n"))
    return number


user_num=pick_num()
rand_num=random.randint(1,100) 
if rand_num==user_num:
    print("success")
else:
    print(f"fail!, your number:{user_num} random number:{rand_num}")


