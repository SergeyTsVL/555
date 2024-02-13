#number = 1
#while number < 100:
    #number = number + 10
    #print(number)
#number1 = 1
#while number1 > 0:
    #number1 = number1 + 10
    #print(number1)

#f1, f2 = 1, 1
#while f1 + f2 < 1000:
#    next_f2 = f1 + f2
#    next_f1 = f2
#    f1, f2 = next_f1, next_f2
#    print(f2)

#my_pets = ("dog", "cat", "monstr111", "monstr222", "monstr333")
#i = 0
#while i < len(my_pets):
#    print("Проверяем", pet)
#    if pet == "cat":
#        print("Нашел кота", pet)
#        break
#    i += 1
#else:
#    print("Ну нет здесь кота")
#print("Чао")



my_pets = ("dog",  "monstr111", "monstr222", "cat","monstr333")
i = -1
while i < len(my_pets):
    i += 1
    if i == 2:
        continue
    print("Проверяем", pet)
    if pet == "cat":
        print("Нашел кота", pet)
        break
print("Чао")