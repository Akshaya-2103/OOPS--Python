from AbstractAccess import AbstractStudent

class Student(AbstractStudent):
    def display_details(self):
        print("Name: ",self.name)
        print("Roll Number: ",self._roll_number)
        print("Password: ",self.__password)

    def get_password(self):
        return self.__password

    def set_password(self,new_password):
        self.__password = new_password