class AbstractFactory:
    def create_engine(self):
        pass

    def create_mover(self):
        pass

    def create_fuel(self):
        pass


class PistonFactory(AbstractFactory):
    """
    Завод поршневых двигателей
    """

    def create_engine(self):
        return 'Создан поршеневой двигатель'


class RotorFactory(AbstractFactory):
    """
    Завод роторных двигателей
    """

    def create_engine(self):
        return 'Создан роторный двигатель'


class ReactiveEngineFactory(AbstractFactory):
    """
    Завод реактивных двигателей
    """

    def create_engine(self):
        return 'Создан реактивный двигатель'


class WheelsFactory(AbstractFactory):
    """
    Завод колес
    """

    def create_mover(self):
        return 'Создано колесо'


class TrackFactory(AbstractFactory):
    """
    Завод гусениц
    """

    def create_mover(self):
        return 'Создана гусеница'


class ScrewFactory(AbstractFactory):
    """
    Завод винтов
    """

    def create_mover(self):
        return 'Создан винт'


class ReactiveMoverFactory(AbstractFactory):
    """
    Завод реактивных сопл
    """

    def create_mover(self):
        return 'Создано реактивное сопло'


class PetrolFuel(AbstractFactory):
    """
    Завод по производству бензина
    """

    def create_mover(self):
        return 'Создано бензиновое топливо'


class DieselFuel(AbstractFactory):
    """
     Завод по производству дизеля
    """

    def create_fuel(self):
        return 'Создано дизельное топливо'


class BatteryFuel(AbstractFactory):
    """
    Завод по производству аккумуляторов
    """

    def create_fuel(self):
        return 'Создан аккумулятор'


class HydrogenFuel(AbstractFactory):
    """
    Завод по производству водорода
    """

    def create_fuel(self):
        return 'Создано водородное топливо'


class UranusFuel(AbstractFactory):
    """
    Завод по производству урана
    """

    def create_fuel(self):
        return 'Создано урановое топливо'


class AntimatterFuel(AbstractFactory):
    """
    Завод по производству антиматерии
    """

    def create_fuel(self):
        return 'Создана антиматерия'


class Client:
    """
    Заказчик транспорта
    """

    def __init__(self, type_transport, fuel_consumption, transport_speed):
        self.type_transport = type_transport
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

    def engine_route(self, factory):
        return factory.create_engine(self)

    def mover_route(self, factory):
        return factory.create_mover(self)

    def fuel_route(self, factory):
        return factory.create_fuel(self)

    def construction(self):
        print(f'Создан {self.type_transport} транспорт')
        print(f'Скорость {self.transport_speed} ед/ч. Расход топлива {self.fuel_consumption} сек')


transport_1 = Client('Наземный', 20, 250)
print(transport_1.engine_route(PistonFactory))
print(transport_1.mover_route(ScrewFactory))
print(transport_1.fuel_route(HydrogenFuel))
transport_1.construction()
