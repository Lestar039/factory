from factory import Factory


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
    __name = 'Водитель'

    def create_driver(self):
        return Person()


class Pilot(AbstractDriver):
    __name = 'Пилот'

    def create_driver(self):
        return Person()


class Captain(AbstractDriver):
    __name = 'Капитан'

    def create_driver(self):
        return Person()


class CreateDriver(AbstractDriver):

    def __init__(self, transport, type_driver, name):
        self.transport = transport
        self.type_driver = type_driver
        self.name = name

    def create_driver(self):
        if self.type_driver == 'Водитель':
            print(f'Создан водитель {self.name}')
            return Driver().create_driver()
        elif self.type_driver == 'Пилот':
            print(f'Создан пилот {self.name}')
            return Pilot().create_driver()
        elif self.type_driver == 'Капитан':
            print(f'Создан катитан {self.name}')
            return Captain().create_driver()


# =====> test CreateDriver <=====
print('=========== Создание транспорта =============')
transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)

print('=========== Создание водителя =============')
driver_1 = CreateDriver(transport_1, 'Пилот', 'Dart Weider').create_driver()
# print(driver_1.create_driver())
