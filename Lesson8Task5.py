# 5 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

from abc import ABC, abstractmethod


class Warehouse:
    devices_in_warehouse = {'Printer': [], 'Scanner': [], 'Copier': []}
    user_devices = {'Printer': [], 'Scanner': [], 'Copier': []}

    @classmethod
    def to_warehouse(cls, *devices, from_user=False):
        if not from_user:
            for device in devices:
                cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
                print(device, 'Принято на склад.')
        else:
            for device in devices:
                cls.user_devices[str(device.__class__.__name__)].remove(device)
                cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
                print(device, 'Принято на склад.')

    @classmethod
    def from_warehouse(cls, device):
        cls.devices_in_warehouse[str(device.__class__.__name__)].remove(device)
        cls.user_devices[str(device.__class__.__name__)].append(device)
        print(device, 'Передано со склада.')

    def __str__(self):
        string_warehouse = '\n'.join(map(str, (sum(self.devices_in_warehouse.values(), []))))
        string_warehouse = 'Устройства на складе:\n' + string_warehouse if string_warehouse else 'На складе нет устройств'
        string_user = '\n'.join(map(str, (sum(self.user_devices.values(), []))))
        string_user = 'Устройства у пользователей:\n' + string_user if string_user else 'У пользователей устройств'
        return string_warehouse + '\n' + string_user


class Device(ABC):
    def __init__(self, brand, serial, owner='зав.складом'):
        self._brand = brand
        self._serial = serial
        self._owner = owner

    def __str__(self):
        return 'Устройство {}, номер {}, ответственный {}.'.format(self._brand, self._serial, self._owner)

    def change_owner(self, owner='зав.складом'):
        print('Устройство {} переписано с {} на {}.'.format(self._brand, self._owner, owner))
        self._owner = owner
        if self._owner == 'зав.складом':
            Warehouse.to_warehouse(self, from_user=True)
        else:
            Warehouse.from_warehouse(self)

    @classmethod
    def how_mush_devices(cls, device='All'):
        if str(device) == 'All':
            string_warehouse = {key: len(value) for key, value in Warehouse.devices_in_warehouse.items()}
            string_user = {key: len(value) for key, value in Warehouse.user_devices.items()}
        else:
            string_warehouse = {device: len(Warehouse.devices_in_warehouse[device])}
            string_user = {device: len(Warehouse.user_devices[device])}
        string_warehouse = 'Устройства на складе:\n' + '\n'.join(
            '{}: {}'.format(key, value) for key, value in string_warehouse.items()) + '\nИтого: ' + str(
            sum(string_warehouse.values()))
        string_user = 'Устройства у пользователей:\n' + '\n'.join(
            '{}: {}'.format(key, value) for key, value in string_user.items()) + '\nИтого: ' + str(
            sum(string_user.values()))
        return string_warehouse + '\n' + string_user

    @abstractmethod
    def work(self):
        print('Устройство {}, номер {} находится на складе.'.format(self._brand, self._serial))


class Printer(Device):
    def work(self):
        if self._owner == 'зав.складом':
            super().work()
        else:
            print('Устройство печатает.')

    @classmethod
    def how_mush_devices(cls, device='Printer'):
        return super().how_mush_devices(device)


class Scanner(Device):
    def work(self):
        if self._owner == 'зав.складом':
            super().work()
        else:
            print('Устройство сканрует.')

    @classmethod
    def how_mush_devices(cls, device='Scanner'):
        return super().how_mush_devices(device)


class Copier(Device):
    def work(self):
        if self._owner == 'зав.складом':
            super().work()
        else:
            print('Устройство копирует.')

    @classmethod
    def how_mush_devices(cls, device='Copier'):
        return super().how_mush_devices(device)


def main():
    print(Warehouse())
    printer = Printer('Xerox', 501)
    scanner = Scanner('HP', 142)
    copier = Copier('Xerox', 673)
    printer_2 = Printer('Canon', 1056)
    print('******************************')
    copier.work()
    print('******************************')
    Warehouse.to_warehouse(printer, scanner, copier, printer_2)
    print('******************************')
    print(Warehouse())
    print('******************************')
    printer.change_owner('Валентин Валентинов')
    print('******************************')
    print(Warehouse())
    print('******************************')
    copier.change_owner('Людвиг Ваныч')
    print('******************************')
    copier.work()
    print('******************************')
    printer.change_owner()
    print('******************************')
    print(Warehouse())
    print('******************************')
    print(Device.how_mush_devices())
    print('******************************')
    print(printer.how_mush_devices())


if __name__ == '__main__':
    main()
