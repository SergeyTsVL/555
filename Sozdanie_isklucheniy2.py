class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass

try:
    raise InvalidDataException('Привет InvalidDataException')
except InvalidDataException as e:
    print(f'Ошибка: {e}')
    raise InvalidDataException('Миссия провалена')
except ProcessingException as e:
    print(f'Внимание: {e}')
finally:
    print('789')

