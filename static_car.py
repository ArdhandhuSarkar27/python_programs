class Car:
    @staticmethod
    def Start():
        print("Car Started")
class Land_Rover(Car):
    def __init__(self, Brand):
        self.Brand = Brand
class Rolls_Royce(Car):
    def __init__(self, Brand):
        self.Brand = Brand
car1 = Land_Rover("Defender")
car1.Start()
car2 = Rolls_Royce("Phantom")
car2.Start()