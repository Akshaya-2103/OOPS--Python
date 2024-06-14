from abc import ABC, abstractmethod

class AbstractStudent:
    def __init__(self, name, roll_number, password):
        self.name = name #Public attribute
        self._roll_number = roll_number #protected attribute
        self.__password = password #Private attribute

    @abstractmethod
    def display_details(self):
        pass

    def get_password(self):
        pass

    def set_password(self,new_password):
        pass