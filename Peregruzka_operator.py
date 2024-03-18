class Buiding:
    def __init__(self, Floors, Types):
        self.numberOfFloors = Floors
        self.buildingType = Types
        print("целочисленный атрибут этажности  и строковый атрибут", int(self.numberOfFloors), str(self.buildingType))
    def __eq__(self, other):


        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

a = Buiding(5, "j")
print(a.__eq__)


