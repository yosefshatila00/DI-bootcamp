class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        amount_str = str(self.amount)
        currency_str = self.currency
        if self.amount == 1:
            return f"{amount_str} {currency_str}"
        else:
            if currency_str.endswith('y'):
                currency_str = currency_str[:-1] + 'ies'
            else:
                currency_str += 's'
            return f"{amount_str} {currency_str}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Currency' and '{type(other).__name__}'")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for +=: 'Currency' and '{type(other).__name__}'")
        

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>