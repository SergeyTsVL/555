class Exception:
    list = [int(1), int(0), 'fv', None]
    print(list)

class InvalidDataException(Exception):
    def rr():
        r = 2
        if list[r] == 'fv':
            raise 'fv'

class ProcessingException(Exception):
    def ff():
        a = 1
        b = 0
        try:
            c = a / b
            print(c)
        except:
            print(f'Я в классе ProcessingException ')
        finally:
            print(f'Прошли finally')

d = ProcessingException
d.ff()
g = InvalidDataException()
print(g.rr)





        # list2 = [g, 5, True, 'dggh']
