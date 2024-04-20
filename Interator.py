class EvenNumbers():
    def __init__(self, start, end):
        self.i, self.start, self.end = start, start, end

    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i % 2 == 0:
            if self.i > self.end:
                raise StopIteration()
            return self.i
        else:
            self.i += 1
            if self.i % 2 == 0:
                # print('\n')
                if self.i > self.end:
                    raise StopIteration()
                return self.i


iter = EvenNumbers(10, 25)
print(iter)
for i in iter:
    print(i)
