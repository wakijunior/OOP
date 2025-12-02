class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "General sound"
    
class Dog(Animal):
    def speak(self):
        return "Barks"
    
class Hoarse (Animal):
    def speak(self):
        return "Neighs"
    
dog1 = Dog("Max")
print(f"The dog {dog1.name} {dog1.speak()} alot")

horse1 = Hoarse("skip")
print(f"My horse named {horse1.name} {horse1.speak()}")
