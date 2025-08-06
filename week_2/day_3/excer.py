class cat():
    def __init__(self, cat_name, cat_age):
        self.name=cat_name
        self.age=cat_age

cat1=cat("memo", 10)
cat2=cat("lion", 15)
cat3=cat("smoky", 4)

def find_old_cat(cat1, cat2, cat3):
    oldest=cat1
    if cat2.age>oldest.age:
        oldest=cat2
    if cat3.age>oldest.age:
        oldest=cat3
    return oldest
    
old=find_old_cat(cat1,cat2,cat3)
print(f"the oldest cat is {old.name}")



class dog():
    def __init__(self,dog_name,dog_height):
        self.name=dog_name
        self.height=dog_height

    def bark(self):
        print(f"{self.name} goes woof")

    def jump(self):
        x=self.height*2
        print(f"jumps {x} cm high")


davids_dog=dog("woofy", 100)
sarahs_dog=dog("kooky",120)

print(f"davids dog is {davids_dog.name} and his height is {davids_dog.height}")
print(f"davids dog is {sarahs_dog.name} and his height is {sarahs_dog.height}")

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()


class song():
    def __init__(self, lyrics):
        self.lyrics=lyrics

    def sing_me_song(self):
        for x in self.lyrics:
            print(x)

stairway = song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])

stairway.sing_me_song()


class Zoo():  
    def __init__(self, zoo_name, animals=None):  
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:  
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo!")  

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:  
            print(animal)
     
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:  
            self.animals.remove(animal_sold)
            print(f"Sold {animal_sold}")
        else:
            print(f"{animal_sold} is not in the zoo!")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)  
        groups = {}
        
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        
        return groups
    
    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


brooklyn_safari = Zoo("Brooklyn Safari")  

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Lion")

print("All animals:")
brooklyn_safari.get_animals()

print("\nSelling an animal:")
brooklyn_safari.sell_animal("Bear")

print("\nRemaining animals:")
brooklyn_safari.get_animals()

print("\nAnimal groups:")
brooklyn_safari.get_groups()