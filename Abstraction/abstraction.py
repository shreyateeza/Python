from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, number_of_tyres):
        self.num_of_tyres = number_of_tyres

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def __init__(self, number_of_tyres, color):
        super().__init__(number_of_tyres)
        self.color = color

    def start(self):
        print("Car is starting")


class Bike(Vehicle):
    def __init__(self, number_of_tyres, color):
        super().__init__(number_of_tyres)
        self.color = color

    def start(self):
        print("bike is starting")


class abcz(Vehicle):
    def start(self):
        print("abcz is start1")


# v = Vehicle() # Not possible; TypeError: Can't instantiate abstract class Vehicle with abstract method start
c = Car(2, "red")
b = Bike(2, "blue")
abx = abcz(1)

def startVehicle(v: Vehicle):
    v.start()

startVehicle(b)
startVehicle(c)