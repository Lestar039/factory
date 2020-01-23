from factory import Factory
from move_description import Route, TranslateMoveCommand


# =====> Базовые классы водителей <=====
class AbstractPerson:
    """
    Базовый класс человека
    """
    def set_command(self, command):
        self.command = command

    def motion_report(self):
        command_handler = TranslateMoveCommand()
        route_move = Route(command_handler.translate_command(self.command)).make_move()
        return route_move


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
    print()
    print('========= Отчет водителя о маршруте =========')
    command_to_moving = driver_1.set_command(['forward 10', 'backward 20', 'left 30', 'right 40'])
    driver_1.motion_report()
