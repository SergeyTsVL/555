class Buiding:
    total = 0
    def __init__(self):
        Buiding.total += 1

number_of_floors = []

while len(number_of_floors) < 5:   # вместо 40 поставил 5. Но всеравно выводит 10 вместо 5
    new_Buiding = Buiding()
    number_of_floors.append(new_Buiding)
    # print(Buiding())
print(Buiding.total)








