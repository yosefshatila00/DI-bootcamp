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



def make_shirt(size="large", text="i love python"):
    print(f"the size of the shirt is {size} and the text is {text}")

make_shirt()
make_shirt("medium", "i love python")
make_shirt("small", "i hate studying")

make_shirt(size="small", text="hello")


magician_names=['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)

def make_great(magician_names):
    for name in magician_names:
        print(f"the great{name}")
    

show_magicians(magician_names)
make_great(magician_names)



def get_random_temp():
    tempo=random.uniform(-10,40)
    return tempo


def main():
    temp=get_random_temp()
    print(f"the temperature right now is {temp} degrees celsius")
    if temp<0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0<=temp<16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16<=temp<=23:
        print("Nice weather.")
    elif 24<=temp<=32:
        print("a bit warm, stay hydrated")
    elif 32<=temp<=40:
        print("Its really hot! Stay cool.")


main()

