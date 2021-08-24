class Car:
    def __init__(self):
        print("Four wheeler")
    def model(self):
        print("Hyundai Creta")
class Bike:
    def __init__(self):
        print("Two wheeler")
    def model(self):
        print("Royal Enfield Classic 350")
class Vehicle(Car, Bike):
    def __init__(self):
        print("Vehicle")

v1 = Vehicle()
v1.model()