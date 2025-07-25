import random

charc=input("enter a string that is 10 characters long:")
b=len(charc)
if b < 10:
    print("String not long enough")
    exit()
elif b > 10:
    print("String too long")
    exit() 
else:
    print("string is perfect")

print(f"first character:{charc[0]}")
print(f"last character:{charc[-1]}")

for i in range(0, len(charc) +1  ):
    print(f"{charc[:i]}")
    
charc= list(charc)
random.shuffle(charc)
charc=''.join(charc)
print(f"shuffled string: {charc}")
