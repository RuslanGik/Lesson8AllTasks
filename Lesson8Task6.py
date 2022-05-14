# 6 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Error(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Storage:
    def __init__(self):
        self.storage = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise Error(f"Error!")

        self.storage.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise Error(f"Недопустимый тип!'")

        item: OfficeEquipment = self.storage[idx]

        item.department = department

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise Error

        return self.storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise Error

        del self.storage[key]

    def __iter__(self):
        return self.storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.storage)} устройств"


class OfficeEquipment:

    def __init__(self, type: str = None, name: str = "", model: str = ""):
        self.type = type
        self.name = name
        self.model = model

        self.department = None

    def __str__(self):
        return f"{self.type} {self.name} {self.model}"

    @staticmethod
    def valid(cnt):
        if not isinstance(cnt, int):
            Error(f"'{type(cnt)}'; количество экземпляров должно быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.valid(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(type='Xerox', **kwargs)


storage = Storage()
storage.add(Printer.create(4, name="Epson", model="1111-400"))
storage.add(Scanner.create(3, name="x4", model="1111-AD"))
storage.add(Scanner.create(2, name="x11", model="5368-AD"))
storage.add(Xerox.create(6, name="Xerox", model="2345"))
print(storage)

print(storage)
del storage[0]
print(storage)