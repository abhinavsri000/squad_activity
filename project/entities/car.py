from ._vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, regno, driver, size = 1):
        self.regno = regno
        self.driver = driver
        self.size = size
