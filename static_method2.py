class Building:
    @staticmethod
    def biggest_building():
        return "This is the biggest building."
    @staticmethod
    def smallest_building():
        return "This is the smallest building."
class Buildings(Building):
    def __init__(self, name):
        self.name = name
building1 = Buildings("Empire State Building")
print(Buildings.smallest_building())
building2 = Buildings("Burj Khalifa")
print(Buildings.biggest_building())