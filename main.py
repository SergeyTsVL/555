import csv

def write_holiday_cities(first_letter):

    with open("travel-notes.csv", mode="r", encoding='utf-8') as file:

        data_list = []
        data_list1 = []
        listing_list = []    # для городов людей, имена которых начинаются на 'L' которые посетили
        listing_list1 = []   # для городов людей, имена которых начинаются на 'L' которые хотят посетить
        listing_list2 = []   # для городов людей, имена которых начинаются на 'L' в которых еще небыли

        for row in csv.reader(file):
            data_list.append(row)
            # print(row[0:1])
            if first_letter in ''.join(row[0:1]):
# цикл для городов людей, имена которых начинаются на 'L' которые посетили
                for i in row[1:2]:
                    j = i.split(';')
                    listing_list.append(j)
# цикл для городов людей, имена которых начинаются на 'L' которые хотят посетить
                for i in row[2:]:
                    j = i.split(';')
                    listing_list1.append(j)
# цикл для городов людей, имена которых начинаются на 'L' в которых еще небыли
            data_list1.append(row)
            for i in row[1:2]:
                j = i.split(';')
                listing_list2.append(j)


# городов людей, имена которых начинаются на 'L' которые посетили
        plenty = set(sum(listing_list, []))
        list_set = list(plenty)
        list_set.sort()
        list_set[0] = 'Посетeли: ' + list_set[0]                     # для вывода в holiday.csv согласно дом.заданию

# для городов людей, имена которых начинаются на 'L' которые хотят посетить
        plenty1 = set(sum(listing_list1, []))
        list_set1 = list(plenty1)
        list_set1.sort()

        # list_set1[0] = 'Xотят посетить:' + list_set1[0]

# для городов людей, имена которых начинаются на 'L' в которых еще небыли
        plenty2 = set(sum(listing_list2, []))
        list_set2 = list(plenty2)
        list_set2.sort()

        list_set2_1 = []
        for element in list_set1:
            if element not in list_set2:
                list_set2_1.append(element)

        list_set1[0] = 'Xотят посетить: ' + list_set1[0]            # для вывода в holiday.csv согласно дом.заданию

# для городa который посетят
        visit_city = list_set2_1[0].split()

        list_set2_1[0] = 'Никогда не были в: ' + list_set2_1[0]      # для вывода в holiday.csv согласно дом.заданию
        visit_city[0] = 'Следующим городом будет: ' + visit_city[0]  # для вывода в holiday.csv согласно дом.заданию

        a = list(list_set)
        b = list(list_set1)
        c = list(list_set2_1)
        d = list(visit_city)




        print(', '.join(list_set))
        print(', '.join(list_set1))
        print(', '.join(list_set2_1))
        print(''.join(visit_city))



        with open("holiday.csv", mode="w", encoding='utf-8', newline='') as out_csv:
            writer = csv.DictWriter(out_csv, fieldnames=a)
            writer.writeheader()
            writer = csv.DictWriter(out_csv, fieldnames=b)
            writer.writeheader()
            writer = csv.DictWriter(out_csv, fieldnames=c)
            writer.writeheader()
            writer = csv.DictWriter(out_csv, fieldnames=d)
            writer.writeheader()

write_holiday_cities('L')
