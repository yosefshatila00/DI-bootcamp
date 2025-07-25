print("hello world \n"*4)

print(99**3*8)

#5 < 3 false
#3 == 3 true 
#3 == "3" error
#"3" > 3error
#"Hello" == "hello" true

computer_brand = "HP"
print(f"I have a {computer_brand} computer")

name="yosef"
age=25
shoe_size=44
info=f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}"
print(info)

a=input("Enter a number: ")
b=input("Enter another number: ")
a = int(a)
b = int(b)  
if a > b:
    print("hello world")


d=input("Enter a number: ")
if int(d) % 2 == 0:
    print("Even")
else:
    print("Odd")



name = input("Enter your name: ")
if name == "yosef":
    print("Hello yosef")
else:
    print("Hello not Yosef ")



height = input("Enter your height in cm: ")
if int(height) >= 145:
    print("You are tall enough for the ride")
else:
    print("You need to grow some more")
