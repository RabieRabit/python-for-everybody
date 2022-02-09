#Main class
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def speak(self):
        print ("What does this animal say?")

#Class inherets from animal
class Dog(Animal):
    #overwrightis animal speak class
    def speak(self):
        print(f"{self.name} the dog ({self.type}) says Woof")

#class inherets from animal
class Cat(Animal):
    #overrights animal speak class
    def speak(self):
        print(f"{self.name} the cat ({self.type}) says Meoooww")

kevin = Dog("Kevin", "Brittish Bulldog")
kevin.speak();

henry = Dog("Henry", "Pitbull")
henry.speak()

rito = Cat("Rito", "Chinese Hairless");
rito.speak()

#Result = Woof
