from factory import Factory


# =====> Создание водителя <=====
class AbstractPersonFactory:
    def create_person(self):
        raise NotImplementedError('Мы тут - AbstractPerson')


class Person(AbstractPersonFactory):
    def create_person(self):
        return 'Создан человек'


# =====> Создание типа водителя  <=====
class AbstractDriverFactory:
    def create_driver(self):
        raise NotImplementedError('Мы тут - AbstractDrive')


class Driver(AbstractDriverFactory):
    def create_driver(self):
        return Person()


class Pilot(AbstractDriverFactory):
    def create_driver(self):
        return Person()


class Captain(AbstractDriverFactory):
    def create_driver(self):
        return Person()


class CreateDriver:

    def create_driver(self, transport, name):
        if transport.type_transport == 'Наземное':
            print(f'Создан водитель: {name}')
            return Driver().create_driver()
        elif transport.type_transport == 'Водное':
            print(f'Создан катитан: {name}')
            return Captain().create_driver()
        elif transport.type_transport == 'Воздушное':
            print(f'Создан пилот: {name}')
            return Pilot().create_driver()


if __name__ == "__main__":
    print('=========== Создание транспорта =============')
    transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)

    print('============ Создание водителя ==============')
    driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
