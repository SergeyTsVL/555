class Buiding:
    def __init__(self, Floors, Types):
        self.numberOfFloors = Floors
        self.buildingType = Types
        print("целочисленный атрибут этажности  и строковый атрибут", int(self.numberOfFloors), str(self.buildingType))

    def __eq__(self, other):

        if self.numberOfFloors == self.buildingType:
            print("True")
            return other

        else:
            print("False")
            return other

a = Buiding(5, "j")

print(a.__eq__)

a.__eq__(7)

