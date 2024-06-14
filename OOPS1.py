class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self,lang):
        print(f"Hi my name is {self.name} and my age is {self.age} and my language is {lang}")

p1=Person("asaya",11)
p2=Person("ammuuu",11)

p1.speak("Malayalam")
