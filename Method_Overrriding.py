#Parent Class
class Animal:
    def speak(self):
        return "Animal makes a sound"

#Child class1
class Dog(Animal):
    def speak(self):
        return "Woof!"

#Child class2
class Cat(Animal):
    def speak(self):
        return "Meow!"

#Child class3 
class Cow(Animal):
    def speak(self):
        pass

dog = Dog()
cat = Cat()
cow = Cow()

print("Dog says: ",dog.speak())
print("Cat says: ",cat.speak())
print("Cow says: ",cow.speak()) 
