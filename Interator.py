class EvenNumbers:
    def __init__(self, start, end):
        self.i, self.start, self.end = start, start, end

    def __iter__(self):
        # self.i, self.start, self.end = 0, 0, 1
        return self
    def __next__(self):
        self.i += 1
        if self.i % 2 == 0 and self.i > self.start:
            # print('\n')
            if self.i > self.end:
                raise StopIteration()
            return self.i



iter = EvenNumbers
print(iter)
for i in iter(100, 150):
    print(i)
print(121 in iter(100, 150))