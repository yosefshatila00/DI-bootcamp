class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class siamese(Cat):
    pass



all_cats = [Bengal("memo", 10), Chartreux("weat", 4), siamese("milo", 12)]
sara_pets=Pets(all_cats)

sara_pets.walk()




class Dog:
    def __init__(self, name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        run=(self.weight)/(self.age*10)
        return run
    
    def fight(self, other_dog):
        mystrength= self.run_speed()*self.weight
        otherstrength=other_dog.run_speed()*other_dog.weight
        if mystrength>otherstrength:
            return self.name
        elif mystrength<otherstrength:
            return other_dog.name
        else:
            return "its a tie"
        

dog1=Dog("keeko",10,25)
dog2=Dog("rex", 13, 9)
dog3=Dog("jog", 4, 20)

print(dog1.bark())
print(dog1.run_speed())
print(dog3.fight(dog1)+" wins")

class Dog:
    def __init__(self, name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        run=(self.weight)/(self.age*10)
        return run
    
    def fight(self, other_dog):
        mystrength= self.run_speed()*self.weight
        otherstrength=other_dog.run_speed()*other_dog.weight
        if mystrength>otherstrength:
            return self.name
        elif mystrength<otherstrength:
            return other_dog.name
        else:
            return "its a tie"
        
import random
class petdog(Dog):
    def __init__(self,name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained=trained
    def train(self):
        print(self.bark())
        self.trained=True
    def play(self, *args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{' '.join(dog_names)} all play together")
    def do_a_trick(self):
        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead"]
        if self.trained==True:
            trick=random.choice(tricks)
            print({trick})
        else:
            print("dog not trained")

if __name__ == "__main__":
    pet1 = petdog("Rex", 3, 15)
    pet2 = petdog("Max", 5, 30)
    pet3 = petdog("Buddy", 2, 10)

    pet1.train()  
    pet1.do_a_trick()  
    pet2.do_a_trick() 
    
    pet1.play(pet2, pet3) 


class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
    
    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
    
    def born(self, first_name, age):
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)
        print(f"Welcome {first_name} {self.last_name} to the family!")
    
    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(f"You are over 18, your parents accept that you will go out with your friends")
                else:
                    print(f"Sorry {first_name}, you are not allowed to go out with your friends.")
                return
        print(f"{first_name} is not a member of this family.")
    
    def family_presentation(self):
        print(f"\n{self.last_name} Family Members:")
        for member in self.members:
            print(f"- {member.first_name} ({member.age} years old)")


if __name__ == "__main__":
    smith_family = Family("Smith")
    
    smith_family.born("John", 45)
    smith_family.born("Jane", 42)
    smith_family.born("Mike", 17)
    smith_family.born("Sarah", 20)
    
    smith_family.check_majority("Mike")
    smith_family.check_majority("Sarah")
    smith_family.check_majority("Alice") 
    
    smith_family.family_presentation()