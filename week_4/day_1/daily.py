# class is a blueprint for creating an object.
# instance is a single object created from a class.
# encapsulation is the bundling of data and methods that operate on that data within one unit.
# abstraction is the concept of hiding the complex reality while exposing only the necessary parts.
# inheritance is a mechanism where a new class inherits properties and behavior (methods) from an existing class.
# multiple inheritance is a feature where a class can inherit from more than one base class.
# polymorphism is the ability to present the same interface for different data types.
# mro is the order in which base classes are searched when executing a method.
import random

class Card:    
    def __init__(self, suit, value):
     
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.suit}', '{self.value}')"

class Deck:
    
    def __init__(self):
        self.cards = []
        self._initialize_deck()
    
    def _initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
 
        if len(self.cards) != 52:
            self._initialize_deck()
        
        random.shuffle(self.cards)
        return self
    
    def deal(self):
       
        if not self.cards:
            raise IndexError("Cannot deal from an empty deck")
        
        return self.cards.pop()
    
    def count(self):
  
        return len(self.cards)
    
    def is_empty(self):
   
        return len(self.cards) == 0
    
    def __str__(self):
        return f"Deck with {len(self.cards)} cards"
    
    def __repr__(self):
        return f"Deck({len(self.cards)} cards)"
    
    def __len__(self):
        return len(self.cards)


if __name__ == "__main__":
    deck = Deck()
    print(f"Initial deck: {deck}")
    
    deck.shuffle()
    print(f"After shuffling: {deck}")
    
    print("\nDealing 5 cards:")
    for i in range(5):
        card = deck.deal()
        print(f"Card {i+1}: {card}")
    
    print(f"\nCards remaining: {deck.count()}")
    
    try:
        while deck.count() > 0:
            deck.deal()
        print(f"\nAfter dealing all cards: {deck}")
        
        deck.deal()
    except IndexError as e:
        print(f"Error: {e}")
    
    deck.shuffle()
    print(f"\nAfter shuffling empty deck: {deck}")
    print(f"First card dealt: {deck.deal()}")