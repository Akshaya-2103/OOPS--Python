from AbstractVehicle import AbstractVehicle

class Bike(AbstractVehicle):
    def display_details(self):
        print("Bike Details:")
        print(f"Color: {self.color}")
        print(f"Number of tyres: {self.num_tyre}")
        print(f"Gears: {self.gears}")

class Car(AbstractVehicle):
    def display_details(self):
        print("Car Details:")
        print(f"Color: {self.color}")
        print(f"Number of tyres: {self.num_tyre}")
        print(f"Gears: {self.gears}")

class Scooty(AbstractVehicle):
    def display_details(self):
        print("Scooty Details:")
        print(f"Color: {self.color}")
        print(f"Number of tyres: {self.num_tyre}")
        print(f"Gears: {self.gears}")