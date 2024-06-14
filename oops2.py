class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def description(self):
        print(f"This is {self.name} and he/she is {self.age}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed= breed

    def description(self):
        print(f"This guy {self.name} is cute and he is {self.age} old. His breed is {self.breed}")

dog=Dog("Simba", 4 , "Golden")
animal = Animal("Eric",  5)

dog.description()
animal.description()