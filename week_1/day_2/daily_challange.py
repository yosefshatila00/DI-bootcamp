number=input("enter a number: ")
length=input("enter a length: ")
 
multiples = []

for i in range(1, int(length) + 1):
    multiples.append(int(number) * i)

print(multiples)


output=""
user_input=input("enter a string: ")

for char in user_input:
    if len(output)==0 or char !=output[-1]:
     output += char

print(output)

