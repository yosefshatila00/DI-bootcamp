class dog :
    def __init__(self, name, age,color, is_trained=False):
        self.name = name
        self.age = age
        self.color = color
        self.is_trained= is_trained

    def walk(self, meters):
        print(f"{self.name} walked {meters} meters.")

    def bark(self):
        print(f"{self.name} says woof!")

    def run(self):
        if self.age < 5:
            print(f"{self.name} is running fast!")
        elif 6<=self.age<=10:
            print(f"{self.name} is running.")
        else:
            print(f"{self.name} doesnot want to run.")


object1=dog("rex", 10, "brown")
dog1= dog("Buddy", 5, "black", True)



dog1.bark()
dog1.run()

dog1.walk(100)