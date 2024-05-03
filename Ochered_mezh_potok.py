import threading
import time

class Table:
    free_tables = []  # колличество свободных столов

    def __init__(self, number, *args, **kwargs):
        self.number = number  # колличество столов

    def bool(self):

        for i in range(0, self.number):  # присваеваем номера столов
            i += 1
            Table.free_tables.append(i)
        return not None

class Cafe:
    visitor_list = []
    def __init__(self, queue, *args, **kwargs):
        self.queue = queue  # очередь посетителей

    def customer_arrival(self):  # моделирует приход посетителя(каждую секунду)
        visitor = 0

        while visitor < self.queue:
            visitor += 1
            time.sleep(0.1)
            Cafe.visitor_list.append(visitor)
            # print(f'Посетитель номер {visitor} прибыл123321')
        return visitor

    def serve_customer(self):  # моделирует обслуживание посетителя. Проверяет наличие свободных столов, в случае
        vis_tabl_dict = {n: Table.free_tables.count(0) for n in Table.free_tables}
        customer_arrival_th = threading.Thread(target=Cafe.customer_arrival(self))
        customer_arrival_th.start()

        while len(Cafe.visitor_list) > 0:
            for f in vis_tabl_dict:
                for j in vis_tabl_dict:
                    if vis_tabl_dict[j] == 0:
                        try:
                            vis_tabl_dict[j] = Cafe.visitor_list[0]
                            if (max(vis_tabl_dict.keys()) != Cafe.visitor_list[0] - j and Cafe.visitor_list[0] <
                                    max(vis_tabl_dict.keys())):
                                print(f'Посетитель номер {Cafe.visitor_list[0]} прибыл333')
                            print(f'Посетитель № {Cafe.visitor_list[0]}  сел за стол {Table.free_tables[j - 1]}')
                            time.sleep(0.1)
                            del Cafe.visitor_list[0]

                        except:
                            return vis_tabl_dict

                    try:
                        if max(vis_tabl_dict.keys()) == Cafe.visitor_list[0] - 1:
                            for v in Cafe.visitor_list:
                                time.sleep(0.2)
                                print(f'Посетитель номер {v} прибыл')
                                print(f'Посетитель номер {v} ожидает свободный стол')
                    except:
                        pass

                print(f'Посетитель номер {vis_tabl_dict[f]} покушал и ушел.')
                vis_tabl_dict[f] = 0

        customer_arrival_th.join()
        return vis_tabl_dict

ff = Table(number=3)
print(ff.bool())

pp = Cafe(20)
print(pp.serve_customer())

