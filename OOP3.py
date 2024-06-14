class Parent:
    def func1(self):
        print("this is func1")
class Child(Parent):
    def func2(self):
        super().func1() 
        print("this is func2")
ob = Child()
ob.func2()