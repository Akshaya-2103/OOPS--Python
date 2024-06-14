class Parent:
    def func1(self):
        print("1")
class Parent2:
    def func2(self):
        print("2")  
class Child(Parent, Parent2):
    def func3(self):
        print("3")

ob = Child()
ob.func1()
ob.func2()
ob.func3()