while True:
    try:
        move=int(input("enter a number to move: "))
        if move <1 or move>9:
            raise exception("choose a number between 1 and 9")
        break

    except exception as e:
        print(e)
        continue 


sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
print(sandwich_orders)

finished_sandwiches = []
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich.")

print("All sandwiches have been made:", finished_sandwiches)

