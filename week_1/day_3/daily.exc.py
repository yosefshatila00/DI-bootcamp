word=input("enter a word:")

char_index={}
for index, char in enumerate(word):

    if char in char_index:
        char_index[char].append(index)
    else:
        char_index[char] = [index]

print( char_index)

print("\n")
print("\n")

items_purchase={"water": "$2", "bread": "$1.5", "milk":"$3", "eggs":"$5"}
wallet="$10"
print(items_purchase.items())
print(wallet)

clean_prices = {}
for item, price in items_purchase.items():
        # Remove dollar sign and commas, then convert to integer
        clean_price = price.replace("$", "").replace(",", "")
        clean_prices[item] =float(clean_price)

wallet=float(wallet.replace("$", ""))

affordable=[]  
for item, price in clean_prices.items():
     if price<=wallet:
          affordable.append(item)


affordable_sorted=sorted(affordable)
if affordable_sorted == []:
    print("nothing affordable")
else:
    print(f"affordable items are:{affordable_sorted}")


