class Bike:
    @staticmethod
    def Start():
        print("Bike Started")
class Royal_Enfield(Bike):
    def __init__(self, Brand):
        self.Brand = Brand
class Kawasaki(Bike):
    def __init__(self, Brand):
        self.Brand = Brand
car1 = Kawasaki("Ninja H2R")
car1.Start()
car2 = Royal_Enfield("Classic 650")
car2.Start()