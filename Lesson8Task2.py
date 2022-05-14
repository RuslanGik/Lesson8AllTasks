# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    pass


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivisionError("Деление на ноль запрещено")

        return Number(float(self) / float(other))


while True:
    try:
        dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
        print(dividend / divider)
    except MyZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
        break
        