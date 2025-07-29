
from datetime import datetime

def get_age(birth_date):
today = datetime.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
return age

def display_cake(candles):
    candle_part = "_" * (5 + candles) + "i" * candles + "_" * (5 + candles)
    print(f"      {candle_part}")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")


birthdate_str = input("Please enter your birthdate in the format DD/MM/YYYY: ")
age = get_age(birthdate)
last_digit = age % 10
candles = last_digit if last_digit != 0 else 10  
