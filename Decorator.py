def sum_three(*args):
    total = 0
    for namber in args:
        total += namber
    return total

def is_prime(func):
    def wrapper(*args, **kwargs):
        k = 0
        result = func(*args, **kwargs)
        for i in range(2, result // 2 + 1):
            if (result % i == 0):
                k = k + 1
        if (k <= 0):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

ff = is_prime(sum_three)
result = ff(2, 3, 6)
print(result)
