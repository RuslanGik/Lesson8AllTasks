# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date='01-01-2001'):
        self.date = date

    @classmethod
    def split_date(cls, date):
        try:
            new_date = tuple(map(int, date.split('-'))) if len(tuple(map(int, date.split('-')))) == 3 else 'Error'
            if new_date == 'Error':
                raise ValueError
            return new_date
        except ValueError:
            print(f'Некорректный ввод.')

    @staticmethod
    def valid_date(date):
        valid_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        try:
            day, month, year = Date().split_date(date)
            if year % 400 != 0 and year % 100 == 0:
                if 1 <= day <= valid_days[month]:
                    return True
            elif year % 400 != 0 and year % 4 != 0:
                if 1 <= day <= valid_days[month]:
                    return True
            else:
                if month == 2 and 1 <= day <= 29:
                    return True
                elif 1 <= day <= valid_days[month]:
                    return True
            raise Exception
        except KeyError:
            print(f'Некорректная дата! Неверно введен месяц')
            return False
        except TypeError:
            return False
        except Exception:
            print(f'Некорректная дата! Неверно введен день')
            return False


def tests():
    date = Date('01-02-2021')
    assert date.split_date(date.date) == (1, 2, 2021)
    assert Date().split_date('31-08-1999') == (31, 8, 1999)
    assert Date().split_date('89-12-1874-1987') == None
    assert Date.valid_date('29-02-2000') == True
    assert Date.valid_date('25-07-2016') == True
    assert Date.valid_date('31-01-2021') == True
    assert Date.valid_date('12-03-1900') == True
    assert Date.valid_date('15-13-1954') == False
    assert Date.valid_date('89-12-1874') == False
    assert Date.valid_date('89-12-1874-1987') == False
    assert Date.valid_date('Not-valid-date') == False
    assert date.valid_date(date.date) == True
    print('All test complite.')


def main():
    while True:
        date = input('Введите дату в формате дд-мм-гг, "q" для выхода или "t" для тестирования: ')
        if date == 'q':
            break
        elif date == 't':
            tests()
            break
        else:
            date = Date(date)
            print(date.split_date(date.date))
            print(date.valid_date(date.date))


if __name__ == '__main__':
    main()
