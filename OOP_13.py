class Engine:
    def start(self):
        return "Vroom! Engine running"

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def drive(self):
        return self.engine.start() + " - Car is moving"

my_car = Car()
print(my_car.drive())