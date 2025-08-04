my_fav_numbers={2,4,6,10}
print("my favorite numbers are:", my_fav_numbers)
my_fav_numbers.add(8)
my_fav_numbers.add(12)
print("my favorite numbers are:", my_fav_numbers)
my_fav_numbers.remove(12)
print("my favorite numbers are:", my_fav_numbers)
friend_fave_number={1, 3, 5, 7}
print("my friend's favorite numbers are:", friend_fave_number)
our_fave_numbers=my_fav_numbers.union(friend_fave_number)
print("our favorite numbers are:", our_fave_numbers)


# tuples are immutable and they can not be changed unless you create a new tuple

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")  
basket.count("Apples")
basket.clear()
print(basket)


#float is a number with decimal point and int is a whole number

list1=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

sequence = []
for i in range(1, 6):
    sequence.append(i - 0.5)  
    sequence.append(i)         
sequence = sequence[:-1]      
print(sequence)


for i in range(21):
    print(i)

for x in range (21):
    if x % 2 == 0:
        print(x, "is even")

name=""
while name !="yousef":
    name=input("enter your name:")
if name == "yousef":
        print("welcome to the club!")


favorite_fruits=[]

number_fruits=int(input("how many fruits do you want to add? "))

for i in range(number_fruits):
    fruit=input(f"enter fruit: ")
    favorite_fruits.append(fruit)

check_fruit=input("enter a fruit to check if it's in your favorite fruits: ")
if check_fruit in favorite_fruits:
    print(f"You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


topping_list=[]
i=0
while topping_list != "quit":
    
    topping=input("enter a topping you want to add to your pizza (or type 'quit' to finish): ")
    
    if topping=="quit":
        break
    else:
        topping_list.append(topping)

print("Your pizza toppings are:", topping_list)

length=len(topping_list)
price=2.5*length+10
print(f"the price is ${price}")



number_people=int(input("how many people are in your group? "))
for i in range(number_people):
    age=int(input(f"enter age of person {i+1}: "))
    if age < 3:
        print("the ticket is free")
    elif age<12:
        print("the ticket is $10")
        price=price+10
    else:
        print("the ticket is $15")
        price=price+15

print(f"the total price is ${price}")

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
print(sandwich_orders)

finished_sandwiches = []
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich.")

print("All sandwiches have been made:", finished_sandwiches)



