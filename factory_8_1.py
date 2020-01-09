# =====> Двигатели <=====
class AbstractEngine:
    def create_engine(self):
        raise NotImplementedError


class PistonFactory(AbstractEngine):
    """
    Завод поршневых двигателей
    """

    def create_engine(self):
        return 'Создан поршневой двигатель'


class RotorFactory(AbstractEngine):
    """
    Завод роторных двигателей
    """

    def create_engine(self):
        return 'Создан роторный двигатель'


class ReactiveFactory(AbstractEngine):
    """
    Завод реактивных двигателей
    """

    def create_engine(self):
        return 'Создан реактивный двигатель'


class EngineFactory:

    def __init__(self, engine):
        self.engine = engine

    def create_engine(self):
        if self.engine == 'Поршневой':
            return PistonFactory().create_engine()
        elif self.engine == 'Роторный':
            return RotorFactory().create_engine()
        elif self.engine == 'Реактивный':
            return ReactiveFactory().create_engine()


# =====> Движители <=====
class AbstractMover:
    def create_mover(self):
        raise NotImplementedError


class WheelsFactory(AbstractMover):
    """
    Завод колес
    """

    def create_mover(self):
        return 'Создано колесо'


class TrackFactory(AbstractMover):
    """
    Завод гусениц
    """

    def create_mover(self):
        return 'Создана гусеница'


class ScrewFactory(AbstractMover):
    """
    Завод винтов
    """

    def create_mover(self):
        return 'Создан винт'


class ReactiveMoverFactory(AbstractMover):
    """
    Завод реактивных сопл
    """

    def create_mover(self):
        return 'Сощдано реактивное сопло'


class MoverFactory(AbstractMover):

    def __init__(self, mover):
        self.mover = mover

    def create_mover(self):
        if self.mover == 'Колесо':
            return WheelsFactory().create_mover()
        elif self.mover == 'Гусеница':
            return TrackFactory().create_mover()
        elif self.mover == 'Винт':
            return ScrewFactory().create_mover()
        elif self.mover == 'Реактивное сопло':
            return ReactiveMoverFactory().create_mover()


# =====> Топливо <=====
class AbstractFuel:
    def create_fuel(self):
        raise NotImplementedError


class PetrolFuel(AbstractFuel):
    """
    Завод по производству бензина
    """

    def create_fuel(self):
        return 'Создано бензиновое топливо'


class DieselFuel(AbstractFuel):
    """
     Завод по производству дизеля
    """

    def create_fuel(self):
        return 'Создано дизельное топливо'


class BatteryFuel(AbstractFuel):
    """
    Завод по производству аккумуляторов
    """

    def create_fuel(self):
        return 'Создан аккумулятор'


class HydrogenFuel(AbstractFuel):
    """
    Завод по производству водорода
    """

    def create_fuel(self):
        return 'Создано водородное топливо'


class UranusFuel(AbstractFuel):
    """
    Завод по производству урана
    """

    def create_fuel(self):
        return 'Создано урановое топливо'


class AntimatterFuel(AbstractFuel):
    """
    Завод по производству антиматерии
    """

    def create_fuel(self):
        return 'Создана антиматерия'


class FuelFactory(AbstractFuel):

    def __init__(self, fuel):
        self.fuel = fuel

    def create_fuel(self):
        if self.fuel == 'Бензин':
            return PetrolFuel().create_fuel()
        elif self.fuel == 'Дизель':
            return DieselFuel().create_fuel()
        elif self.fuel == 'Электричество':
            return BatteryFuel().create_fuel()
        elif self.fuel == 'Водород':
            return HydrogenFuel().create_fuel()
        elif self.fuel == 'Уран':
            return UranusFuel().create_fuel()
        elif self.fuel == 'Антиматерия':
            return AntimatterFuel().create_fuel()


# =====> Завод <=====
class Factory:
    def __init__(
            self, type_transport, engine, number_engine, mover,
            number_mover, fuel, fuel_consumption, transport_speed
    ):
        self.type_transport = type_transport
        self.engine = engine
        self.number_engine = number_engine
        self.mover = mover
        self.number_mover = number_mover
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

    def create_engine(self):
        for number in range(self.number_engine):
            number = EngineFactory(self.engine).create_engine()
            print(number)

    def create_mover(self):
        for number in range(self.number_mover):
            number = MoverFactory(self.mover).create_mover()
            print(number)

    def create_fuel(self):
        return FuelFactory(self.fuel).create_fuel()

    def specifications(self):
        print(f'Создан {self.type_transport} транспорт')
        print(f'Расход топлива: {self.fuel_consumption} единиц на 1 ед. расстояния')
        print(f'Скорость: {self.transport_speed} ед/ч')


# ==> Test Engine, Mover, Fuel Factories <==
# engine_1 = EngineFactory('Роторный')
# print(engine_1.create_engine())
# mover_1 = MoverFactory('Колесо')
# print(mover_1.create_mover())
# fuel_1 = FuelFactory('Бензин')
# print(fuel_1.create_fuel())
# ===========================
transport_1 = Factory('Наземный', 'Поршневой', 4, 'Колесо', 3, 'Бензин', 20, 2000)
transport_1.create_engine()
transport_1.create_mover()
print(transport_1.create_fuel())
transport_1.specifications()
