import random
from multiprocessing import Process

summ_operation = []
products = []
cash_operation1 = []
data = {}


class WarehouseManager:

    def __init__(self, product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product = product

    def run(self):
        global data
        for j in range(5):

            r = ['receipt', 'shipment']
            random_indeks = int(random.randrange(len(r)))
            cash_operation = r[random_indeks]
            cash_operation1.append(cash_operation)
            # print(cash_operation1)
            if cash_operation == 'receipt':
                t = int(random.randint(0, 500))
                summ_operation.append(t)
            else:
                f = (- 1) * int(random.randint(0, 500))
                summ_operation.append(f)
            data = dict(zip(products, summ_operation))
            products.append(self.product)

        print(cash_operation1, summ_operation)
        print(data)
        return


if __name__ == '__main':
    thread_1 = Process(target=WarehouseManager.run)
    # thread_2 = WarehouseManager(product='product2')
    thread_1.start()
    # thread_2.start()
    thread_1.join()
    # thread_2.join()

# ff = WarehouseManager(product='product1')
# print(ff.run())
# ff = WarehouseManager(product='product2')
# print(ff.run())
