# =====> Двигатели <=====
class AbstractEngine:
    def engine(self):
        raise NotImplementedError


class PistonEngine(AbstractEngine):
    def engine(self):
        return 'Поршневой двигатель'


class RotorEngine(AbstractEngine):
    def engine(self):
        return 'Роторный двигатель'


class ReactiveEngine(AbstractEngine):
    def engine(self):
        return 'Реактивный двигатель'


# =====> Заводы двигателей <=====
class AbstractEngineFactory:
    def create_engine(self):
        raise NotImplementedError


class PistonFactory(AbstractEngineFactory):
    """
    Завод поршневых двигателей
    """
    def create_engine(self):
        return PistonEngine().engine()


class RotorFactory(AbstractEngineFactory):
    """
    Завод роторных двигателей
    """
    def create_engine(self):
        return RotorEngine().engine()


class ReactiveFactory(AbstractEngineFactory):
    """
    Завод реактивных двигателей
    """
    def create_engine(self):
        return ReactiveEngine().engine()


class EngineFactory(AbstractEngineFactory):

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
    def mover(self):
        raise NotImplementedError


class WheelsMover(AbstractMover):
    def mover(self):
        return 'Колесо'


class TrackMover(AbstractMover):
    def mover(self):
        return 'Гусеница'


class ScrewMover(AbstractMover):
    def mover(self):
        return 'Винт'


class ReactiveMover(AbstractMover):
    def mover(self):
        return 'Реактивный двигатель'


# =====> Заводы движителей <=====
class AbstractMoverFactory:
    def create_mover(self):
        raise NotImplementedError


class WheelsFactory(AbstractMoverFactory):
    """
    Завод колес
    """
    def create_mover(self):
        return WheelsMover().mover()


class TrackFactory(AbstractMoverFactory):
    """
    Завод гусениц
    """
    def create_mover(self):
        return TrackMover().mover()


class ScrewFactory(AbstractMoverFactory):
    """
    Завод винтов
    """
    def create_mover(self):
        return ScrewMover().mover()


class ReactiveMoverFactory(AbstractMoverFactory):
    """
    Завод реактивных сопл
    """
    def create_mover(self):
        return ReactiveMover().mover()


class MoverFactory(AbstractMoverFactory):

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
    def fuel(self):
        raise NotImplementedError


class PetrolFuel(AbstractFuel):
    def fuel(self):
        return 'Бензин'


class DieselFuel(AbstractFuel):
    def fuel(self):
        return 'Дизель'


class BatteryFuel(AbstractFuel):
    def fuel(self):
        return 'Батарея'


class HydrogenFuel(AbstractFuel):
    def fuel(self):
        return 'Водород'


class UranusFuel(AbstractFuel):
    def fuel(self):
        return 'Уран'


class AntimatterFuel(AbstractFuel):
    def fuel(self):
        return 'Антиматерия'


# =====> Топливные заводы <=====
class AbstractFuelFactory:
    def create_fuel(self):
        raise NotImplementedError


class PetrolFuelFactory(AbstractFuelFactory):
    """
    Завод по производству бензина
    """
    def create_fuel(self):
        return PetrolFuel().fuel()


class DieselFuelFactory(AbstractFuelFactory):
    """
     Завод по производству дизеля
    """
    def create_fuel(self):
        return DieselFuel().fuel()


class BatteryFuelFactory(AbstractFuelFactory):
    """
    Завод по производству аккумуляторов
    """
    def create_fuel(self):
        return BatteryFuel().fuel()


class HydrogenFuelFactory(AbstractFuelFactory):
    """
    Завод по производству водорода
    """
    def create_fuel(self):
        return HydrogenFuel().fuel()


class UranusFuelFactory(AbstractFuelFactory):
    """
    Завод по производству урана
    """
    def create_fuel(self):
        return UranusFuel().fuel()


class AntimatterFuelFactory(AbstractFuelFactory):
    """
    Завод по производству антиматерии
    """
    def create_fuel(self):
        return AntimatterFuel().fuel()


class FuelFactory(AbstractFuelFactory):

    def __init__(self, fuel):
        self.fuel = fuel

    def create_fuel(self):
        if self.fuel == 'Бензин':
            return PetrolFuelFactory().create_fuel()
        elif self.fuel == 'Дизель':
            return DieselFuelFactory().create_fuel()
        elif self.fuel == 'Электричество':
            return BatteryFuelFactory().create_fuel()
        elif self.fuel == 'Водород':
            return HydrogenFuelFactory().create_fuel()
        elif self.fuel == 'Уран':
            return UranusFuelFactory().create_fuel()
        elif self.fuel == 'Антиматерия':
            return AntimatterFuelFactory().create_fuel()


# =====> Завод <=====
class Factory:

    def create(
            self, type_transport, engine, count_engine, mover,
            count_mover, fuel, fuel_consumption, transport_speed
    ):
        for count in range(count_engine):
            print(EngineFactory(engine).create_engine())

        for count in range(count_mover):
            print(MoverFactory(mover).create_mover())

        print(FuelFactory(fuel).create_fuel())
        print(f'Создан {type_transport} транспорт')
        print(f'Расход топлива: {fuel_consumption} единиц на 1 ед. расстояния')
        print(f'Скорость: {transport_speed} ед/ч')


transport_1 = Factory().create('Наземный', 'Поршневой', 2, 'Колесо', 1, 'Бензин', 20, 200)
