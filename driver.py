from factory import Factory
from move_description import DistanceDirection, RotationDirection


# =====> Базовые классы водителей <=====
class AbstractPerson:
    """
    Базовый класс человека
    """

    def set_transport(self, transport):
        """
        Передаем трпнспорт пилоту
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

        for moving in self.command.command_moving:

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
                break

        if self.transport.fuel.total <= 0:
            pass
        else:
            print('Прибыли на место назначения')


class Driver(AbstractPerson):
    """
    Базовый класс водителя
    """

    def motion_report(self):
        super().motion_report()


class Pilot(AbstractPerson):
    """
    Базовый класс пилота
    """

    def motion_report(self):
        super().motion_report()


class Captain(AbstractPerson):
    """
    Базовый класс капитана
    """

    def motion_report(self):
        super().motion_report()


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
class CreateDriver:
    """
    Создание водителей
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
    transport_1 = Factory().create(
        'НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 200, 2, 90)
    print()
    print('============ Создание водителя ==============')
    driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
