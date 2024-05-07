from multiprocessing import Process, Manager


class WarehouseManager:

    def __init__(self):
        # super().__init__(*args, **kwargs)
        self.product = Manager().dict()

    def process_request(self, request):
        product1, action, amuont = request
        if action == 'receipt':
            if product1 in self.product:
                self.product[product1] += amuont
            else:
                self.product[product1] = amuont
        elif action == 'shipment':
            if product1 in self.product and self.product[product1] >= amuont:
                self.product[product1] -= amuont

    def run(self, request):
        processes = []
        for i in request:
            process = Process(target=self.process_request, args=(i, ))
            processes.append(process)
            process.start()
        for j in processes:
            j.join()
if __name__ == '__main__':
    ff = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    ff.run(requests)
    print(dict(ff.product))

