class House:

    numberOfFloors = 10
    the_desired_floor = 7

    while numberOfFloors > the_desired_floor:
        numberOfFloors -= 1
        print(f"Текущий этаж равен", numberOfFloors,", а нам нужен", the_desired_floor)

print(f"Наш этаж", House.the_desired_floor)