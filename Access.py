class Student:
    def __init__(self, name, roll_number, password):
        self.name = name #Public attribute
        self._roll_number = roll_number #protected attribute
        self.__password = password #Private attribute

    def display_details(self):
        print("Name: ",self.name)
        print("Roll Number: ",self._roll_number)
        print("Password: ",self.__password)

    def get_password(self):
        return self.__password

    def set_password(self,new_password):
        self.__password = new_password

student = Student("OM","A001","OM1234")
print("Name (Public):", student.name)
print("Roll Number (Protected):", student._roll_number)
print("Password (Private):", student.get_password())
