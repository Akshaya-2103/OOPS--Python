class Parent:
    def first(self):
        print("first function")

class Child(Parent):
    def second(self):
        print("second fucntion")

ob = Child()
ob.first()
ob.second()