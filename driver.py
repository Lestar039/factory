from factory import Factory
from move_description import TextDescriptionMove


# =====> Создание водителя <=====
class AbstractPerson:
    def create_person(self):
        raise NotImplementedError('Мы тут - AbstractPerson')


class Person(AbstractPerson):
    def create_person(self):
        return 'Создан человек'


# =====> Создание типа водителя  <=====
class AbstractDriver:
    def create_driver(self):
        raise NotImplementedError('Мы тут - AbstractDrive')


class Driver(AbstractDriver):
    _name = 'Водитель'

    def create_driver(self):
        return Person()


class Pilot(AbstractDriver):
    _name = 'Пилот'

    def create_driver(self):
        return Person()


class Captain(AbstractDriver):
    _name = 'Капитан'

    def create_driver(self):
        return Person()


class CreateDriver(AbstractDriver):

    def __init__(self, transport, name):
        self.transport = transport
        self.name = name

    def create_driver(self):
        if self.transport.type_transport == 'Наземное':
            print(f'Создан водитель: {self.name}')
            return Driver().create_driver()
        elif self.transport.type_transport == 'Водное':
            print(f'Создан катитан: {self.name}')
            return Captain().create_driver()
        elif self.transport.type_transport == 'Воздушное':
            print(f'Создан пилот: {self.name}')
            return Pilot().create_driver()


# =====> test CreateDriver <=====
# print('=========== Создание транспорта =============')
# transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
#
# print('============ Создание водителя ==============')
# driver_1 = CreateDriver(transport_1, 'Dart Weider').create_driver()
