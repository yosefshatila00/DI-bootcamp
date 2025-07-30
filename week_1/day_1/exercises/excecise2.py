print("hello world\n"*4 +"i love python\n"*4)
 
month= input("enter a month from 1 to 12: ")
month = int(month)                


if 3<=month<=5:
    print("It's spring!")
elif 6<=month<=8:
    print("It's summer!")   
elif 9<=month<=11:
    print("It's autumn!")
elif month==12 or month==1 or month==2:
    print("It's winter!")   

