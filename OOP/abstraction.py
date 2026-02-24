#abstraction
from abc import ABC, ABC, abstractmethod


class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("Car is starting")
class bike(vehicle):
    def start(self):
        print("Bike is starting")

my_car = car()
my_car.start()  # Output: Car is starting
my_bike = bike()
my_bike.start()  # Output: Bike is starting
