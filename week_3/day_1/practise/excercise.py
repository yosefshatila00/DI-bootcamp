# class parents:
#     def speak(slef):
#         print(f"parents speaking")

# class child(parents):
#     def speak(self):
#         print(f"child speaking")
# class grandchild(child):
#     pass

# obj1=child()
# obj1.speak()
# obj2=grandchild()
# obj2.speak()


class animal:
    def __init__(self,name,family,legs):
        self.name=name
        self.family=family
        self.legs=legs
    def sleep(self):
        return f"{self.name}is sleeping from animal class"
class dog(animal):
    def __init__(self,name ,family,legs, friendly, age,nickname):
        super().__init__(name,family,legs)
        self.friendly=friendly
        self.age=age    
        self.nickname=nickname
class alien:
    def __init__(self,name,planet):
        self.personal_name=name
        self.planet = planet

class alien_dog(alien, dog):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        
dog1=dog("rex","canine",4, True, 5)
print(dog1.bark())
print(dog1.sleep())





