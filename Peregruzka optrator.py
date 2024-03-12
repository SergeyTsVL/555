class Buiding:
    def __init__(self, Floors, Types):
        self.numberOfFloors = Floors
        self.buildingType = Types
        print(f"целочисленный атрибут этажности  и строковый атрибут", int(self.numberOfFloors), str(self.buildingType))
    def __eq__(self):
        self.d = self.numberOfFloors + self.buildingType
        print(self.d)


a = Buiding(5, "g")
print(a.__init__)
print(a.__eq__)

