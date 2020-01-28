from factory import Factory
from move_description import DistanceDirection, RotationDirection


# =====> Базовые классы водителей <=====
class AbstractPerson:
    """
    Базовый класс человека
    """

    _name = 'abstract person'

    def set_transport(self, transport):
        """
        Передаем транспорт пилоту
        """
        self.transport = transport

    def set_command(self, command):
        """
        Передаем пилоту список команд движения
        """
        self.command = command

    def motion_report(self):
        """
        Отчет пилота и всех запчастей о пройденом пути
        Контроль расхода топлива
        """

        for moving in self.command:

            if moving.direction == DistanceDirection.Forward:
                print(f'{self.transport._name} {self.transport.move_type()} вперед {moving.distance} ед.')
                self.transport.move(moving.distance)
            elif moving.direction == DistanceDirection.Backward:
                print(f'{self.transport._name} {self.transport.move_type()} назад {moving.distance} ед.')
                self.transport.move(moving.distance)

            elif moving.direction == RotationDirection.Left:
                print(f'{self.transport._name} поворачивает {moving.rotate} градусов')
            elif moving.direction == RotationDirection.Right:
                print(f'{self.transport._name} поворачивает {moving.rotate} градусов')

            if self.transport.fuel.total <= 0:
                print('Закончилось топливо')
                return

        print('Прибыли на место назначения')


class Driver(AbstractPerson):
    """
    Базовый класс водителя
    """
    _name = 'водитель'


class Pilot(AbstractPerson):
    """
    Базовый класс пилота
    """
    _name = 'пилот'


class Captain(AbstractPerson):
    """
    Базовый класс капитана
    """
    _name = 'капитан'


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


# =====> Создание водителей <=====
class CreateDriverRouter:
    """
    Роутер водителей
    """

    def engine_type_router(self, transport):
        if transport.type_transport == 'Наземное':
            return DriverFactory()
        elif transport.type_transport == 'Водное':
            return CaptainFactory()
        elif transport.type_transport == 'Воздушное':
            return PilotFactory()


class CreateDriver:
    """
    Создание водителей
    """

    def create_driver(self, transport, name):
        driver = CreateDriverRouter().engine_type_router(transport).create_driver()
        print(f'Создан водитель: {name}')
        return driver


if __name__ == "__main__":
    print('=========== Создание транспорта =============')
    transport_1 = Factory().create(
        'НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 200, 2, 90)
    print()
    print('============ Создание водителя ==============')
    driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
