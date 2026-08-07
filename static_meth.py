class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def is_motor_vehicle():
        return True

    @staticmethod
    def get_vehicle_type():
        return "Car"
print(Car.is_motor_vehicle())
print(Car.get_vehicle_type())