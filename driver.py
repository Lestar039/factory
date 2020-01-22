from factory import Factory


# =====> Базовые классы водителей <=====
class AbstractPerson:
    """
    Базовый класс человека
    """

    def motion_report(self):
        return 'Создан человек'


class Driver(AbstractPerson):
    """
    Базовый класс водителя
    """

    def motion_report(self):
        return 'Вожу ТС'


class Pilot(AbstractPerson):
    """
    Базовый класс пилота
    """

    def motion_report(self):
        return 'Пилотирую на ТС'


class Captain(AbstractPerson):
    """
    Базовый класс капитана
    """

    def motion_report(self):
        return 'Плыву на ТС'


# =====> Фабрика водителей <=====
class AbstractDriverFactory:
    """
    Создание абстрактного водителя
    """

    def create_driver(self):
        raise NotImplementedError('Мы тут - AbstractDrive')


class DriverFactory(AbstractDriverFactory):
    """
    Создание водителя
    """

    def create_driver(self):
        return Driver()


class PilotFactory(AbstractDriverFactory):
    """
    Создание водителя
    """

    def create_driver(self):
        return Pilot()


class CaptainFactory(AbstractDriverFactory):
    """
    Создание водителя
    """

    def create_driver(self):
        return Captain()


class CreateDriver:
    """
    Создание конкретного водителя
    """

    def create_driver(self, transport, name):
        if transport.type_transport == 'Наземное':
            print(f'Создан водитель: {name}')
            return DriverFactory().create_driver()
        elif transport.type_transport == 'Водное':
            print(f'Создан катитан: {name}')
            return CaptainFactory().create_driver()
        elif transport.type_transport == 'Воздушное':
            print(f'Создан пилот: {name}')
            return PilotFactory().create_driver()


if __name__ == "__main__":
    print('=========== Создание транспорта =============')
    transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 200, 2, 90)

    print('============ Создание водителя ==============')
    driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
