from ._vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, regno, age, size = 1):
        self.regno = regno
        self.age = age
        self.size = size
