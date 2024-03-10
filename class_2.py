class House:
    def __init__(self):
        self.numberOfFloors = 0
        print('создан объект с параметром self.numberOfFloors = ', self.numberOfFloors)
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('я внутри метода setNewNumberOfFloors(floors)')
        print('floors', floors)
        print('self.numberOfFloors', self.numberOfFloors)
dom = House()

dom.setNewNumberOfFloors(5)
