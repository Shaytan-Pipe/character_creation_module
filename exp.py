from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданнго числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень из твоего числа."""
    var_1 = calculate_square_root(your_number)
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {var_1}')


print(message)
calc(25.5)
