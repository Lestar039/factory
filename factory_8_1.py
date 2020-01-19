# =====> Двигатели <=====
class AbstractEngine:
    def work(self):
        raise NotImplementedError


class PistonEngine(AbstractEngine):
    __name = 'Поршневой двигатель'

    def work(self):
        return 'Поршневой двигатель работает'


class RotorEngine(AbstractEngine):
    __name = 'Роторный двигатель'

    def work(self):
        return 'Роторный двигатель работает'


class ReactiveEngine(AbstractEngine):
    __name = 'Реактивный двигатель'

    def work(self):
        return 'Реактивный двигатель работает'


# =====> Заводы двигателей <=====
class AbstractEngineFactory:
    def create_engine(self):
        raise NotImplementedError


class PistonFactory(AbstractEngineFactory):
    """
    Завод поршневых двигателей
    """

    def create_engine(self):
        return PistonEngine()


class RotorFactory(AbstractEngineFactory):
    """
    Завод роторных двигателей
    """

    def create_engine(self):
        return RotorEngine()


class ReactiveFactory(AbstractEngineFactory):
    """
    Завод реактивных двигателей
    """

    def create_engine(self):
        return ReactiveEngine()


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
    def move(self):
        raise NotImplementedError


class WheelsMover(AbstractMover):
    __name = 'Колесо'

    def move(self):
        return 'Колесо крутится'


class TrackMover(AbstractMover):
    __name = 'Гусеница'

    def move(self):
        return 'Гусеница крутится'


class ScrewMover(AbstractMover):
    __name = 'Винт'

    def move(self):
        return 'Винт крутится'


class ReactiveMover(AbstractMover):
    __name = 'Реактивное сопло'

    def move(self):
        return 'Реактивное сопло работает'


# =====> Заводы движителей <=====
class AbstractMoverFactory:
    def create_mover(self):
        raise NotImplementedError


class WheelsFactory(AbstractMoverFactory):
    """
    Завод колес
    """

    def create_mover(self):
        return WheelsMover()


class TrackFactory(AbstractMoverFactory):
    """
    Завод гусениц
    """

    def create_mover(self):
        return TrackMover()


class ScrewFactory(AbstractMoverFactory):
    """
    Завод винтов
    """

    def create_mover(self):
        return ScrewMover()


class ReactiveMoverFactory(AbstractMoverFactory):
    """
    Завод реактивных сопл
    """

    def create_mover(self):
        return ReactiveMover()


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
    def burn(self):
        raise NotImplementedError


class PetrolFuel(AbstractFuel):
    __name = 'Бензин'

    def burn(self):
        return 'Расходуется бензин'


class DieselFuel(AbstractFuel):
    __name = 'Дизель'

    def burn(self):
        return 'Расходуется дизель'


class BatteryFuel(AbstractFuel):
    __name = 'Батарея'

    def burn(self):
        return 'Расходуется батарея'


class HydrogenFuel(AbstractFuel):
    __name = 'Водород'

    def burn(self):
        return 'Расходуется водород'


class UraniumFuel(AbstractFuel):
    __name = 'Уран'

    def burn(self):
        return 'Расходуется уран'


class AntimatterFuel(AbstractFuel):
    __name = 'Антиматерия'

    def burn(self):
        return 'Расходуется антиматерия'


# =====> Топливные заводы <=====
class AbstractFuelFactory:
    def create_fuel(self):
        raise NotImplementedError


class PetrolFuelFactory(AbstractFuelFactory):
    """
    Завод по производству бензина
    """

    def create_fuel(self):
        return PetrolFuel()


class DieselFuelFactory(AbstractFuelFactory):
    """
     Завод по производству дизеля
    """

    def create_fuel(self):
        return DieselFuel()


class BatteryFuelFactory(AbstractFuelFactory):
    """
    Завод по производству аккумуляторов
    """

    def create_fuel(self):
        return BatteryFuel()


class HydrogenFuelFactory(AbstractFuelFactory):
    """
    Завод по производству водорода
    """

    def create_fuel(self):
        return HydrogenFuel()


class UranusFuelFactory(AbstractFuelFactory):
    """
    Завод по производству урана
    """

    def create_fuel(self):
        return UraniumFuel()


class AntimatterFuelFactory(AbstractFuelFactory):
    """
    Завод по производству антиматерии
    """

    def create_fuel(self):
        return AntimatterFuel()


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


# ====> Тип танспортного средства <=====
class AbstractTransport:

    def __init__(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        self.name = name
        self.type_transport = type_transport
        self.engine = engine
        self.mover = mover
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

    def move(self):
        raise NotImplementedError


class GroundTransport(AbstractTransport):
    __name = 'Наземный транспорт'

    def move(self):
        return 'Едет'


class WaterTransport(AbstractTransport):
    __name = 'Водный транспорт'

    def move(self):
        return 'Плывет'


class AirTransport(AbstractTransport):
    __name = 'Воздушный транспорт'

    def move(self):
        return 'Летит'


class AbstractTransportFactory:

    def __init__(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        self.name = name
        self.type_transport = type_transport
        self.engine = engine
        self.mover = mover
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

    def create_transport(self):
        raise NotImplementedError


class GroundTransportFactory(AbstractTransportFactory):
    """
    Завод наземного транспорта
    """

    def create_transport(self):
        return GroundTransport(self.name, self.type_transport, self.engine, self.mover,
                               self.fuel_type, self.fuel_consumption, self.transport_speed)


class WaterTransportFactory(AbstractTransportFactory):
    """
    Завод водного транспорта
    """

    def create_transport(self):
        return WaterTransport(self.name, self.type_transport, self.engine, self.mover,
                              self.fuel_type, self.fuel_consumption, self.transport_speed)


class AirTransportFactory(AbstractTransportFactory):
    """
    Завод воздушного транспорта
    """

    def create_transport(self):
        return AirTransport(self.name, self.type_transport, self.engine, self.mover,
                            self.fuel_type, self.fuel_consumption, self.transport_speed)


class TransportFactory(AbstractTransportFactory):
    """
    Завод различных типов ТС
    """

    def create_transport(self):
        if self.type_transport == 'Наземное':
            return GroundTransportFactory(self.name, self.type_transport, self.engine, self.mover, self.fuel_type,
                                          self.fuel_consumption, self.transport_speed).create_transport()
        elif self.type_transport == 'Водное':
            return WaterTransportFactory(self.name, self.type_transport, self.engine, self.mover, self.fuel_type,
                                         self.fuel_consumption, self.transport_speed).create_transport()
        elif self.type_transport == 'Воздушное':
            return AirTransportFactory(self.name, self.type_transport, self.engine, self.mover, self.fuel_type,
                                       self.fuel_consumption, self.transport_speed).create_transport()


# =====> test TransportFactory <=====
# tr_1 = TransportFactory('Катер', 'Водное', 'Пошневой', 'Винт', 'Дизель', 2, 80)
# print(tr_1.create_transport())
# print()


class Factory:
    """
    Завод по сборке транспортных средств
    """

    def create(
            self, name, type_transport, engine, count_engine, mover,
            count_mover, fuel_type, fuel_consumption, transport_speed
    ):
        engine_list = []
        for one_engine in range(count_engine):
            engine_list.append(EngineFactory(engine).create_engine())

        mover_list = []
        for one_mover in range(count_mover):
            mover_list.append(MoverFactory(mover).create_mover())

        new_fuel_type = FuelFactory(fuel_type).create_fuel()

        new_transport = TransportFactory(name, type_transport, engine_list, mover_list, new_fuel_type,
                                         fuel_consumption, transport_speed).create_transport()

        print(f'Создано ТС: {name}')

        return new_transport


# =====> test Factory <=====
print('=========== Создание транспорта =============')
transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
print()


# =====> Заправленное топливо <=====
class AbstractFuelingFuel:
    def refueling_fuel(self):
        raise NotImplementedError('Мы тут - Заправленное топливо')


class PetrolFuelingFuel(AbstractFuelingFuel):
    def refueling_fuel(self):
        return 'Заправляем бензин'


class DieselFuelingFuel(AbstractFuelingFuel):
    def refueling_fuel(self):
        return 'Заправляем дизель'


class ElectricFuelingFuel(AbstractFuelingFuel):
    def refueling_fuel(self):
        return 'Заряжаем батареи'


class HydrogenFuelingFuel(AbstractFuelingFuel):
    def refueling_fuel(self):
        return 'Заправляем водород'


class UraniumFuelingFuel(AbstractFuelingFuel):
    def refueling_fuel(self):
        return 'Заправляем уран'


class AntimatterFuelingFuel(AbstractFuelingFuel):
    def refueling_fuel(self):
        return 'Заправляем антиматерию'


# =====> Виды заправочных станций <=====
class AbstractFuelingStation:
    def add_fuel(self):
        raise NotImplementedError('А теперь мы тут - Виды заправочных станций')


class PetrolFuelingStation(AbstractFuelingStation):
    __name = 'Станция для заправки бензина'

    def add_fuel(self):
        return PetrolFuelingFuel()


class DieselFuelingStation(AbstractFuelingStation):
    __name = 'Станция для заправки дизеля'

    def add_fuel(self):
        return DieselFuelingFuel()


class ElectricFuelingStation(AbstractFuelingStation):
    __name = 'Станция для зарядки батарей'

    def add_fuel(self):
        return ElectricFuelingFuel()


class HydrogenFuelingStation(AbstractFuelingStation):
    __name = 'Станция для заправки водорода'

    def add_fuel(self):
        return HydrogenFuelingFuel()


class UraniumFuelingStation(AbstractFuelingStation):
    __name = 'Станция для заправки урана'

    def add_fuel(self):
        return UraniumFuelingFuel()


class AntimatterFuelingStation(AbstractFuelingStation):
    __name = 'Станция для заправки антиматерии'

    def add_fuel(self):
        return AntimatterFuelingFuel()


# =====> Выбор заправочной станции <=====
class FuelStation(AbstractFuelingStation):
    """
    Выбор заправочной станции в зависимости от типа топлива
    """

    def __init__(self, type_fuel):
        self.type_fuel = type_fuel

    def add_fuel(self):
        if self.type_fuel == 'Бензин':
            return PetrolFuelingStation().add_fuel()
        elif self.type_fuel == 'Дизель':
            return DieselFuelingStation().add_fuel()
        elif self.type_fuel == 'Электричество':
            return ElectricFuelingStation().add_fuel()
        elif self.type_fuel == 'Водород':
            return HydrogenFuelingStation().add_fuel()
        elif self.type_fuel == 'Уран':
            return UraniumFuelingStation().add_fuel()
        elif self.type_fuel == 'Антиматерия':
            return AntimatterFuelingStation().add_fuel()
        else:
            return 'Такой заправки не существует'


# =====> test <=====
# station_1 = FuelStation('Бензин').add_fuel()
# print(station_1.refueling_fuel())


class FuelingTransport:
    """
    Заправочная станция
    """

    def __init__(self, transport, type_fuel, count_fuel):
        self.transport = transport
        self.type_fuel = type_fuel
        self.count_fuel = count_fuel

    def fueling(self):
        new_fuel = FuelStation(self.type_fuel).add_fuel()
        print(f'{self.transport.name} заправлен топливом: {self.type_fuel} - {self.count_fuel} ед.')
        return new_fuel


print('=========== Заправка транспорта =============')
fuel_1 = FuelingTransport(transport_1, 'Антиматерия', 400).fueling()
print()


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
print('=========== Создание водителя =============')
driver_1 = CreateDriver(transport_1, 'Пилот', 'Dart Weider').create_driver()


# class TextDescriptionMove:
#     """
#     Текстовое описание маршрута
#     """
#
#     def __init__(self, transport):
#         self.transport = transport
#
#     def movement_transport(self, movement):
#         # разбиваем маршрут на направление и количество единиц(градусов)
#         direction_of_travel = movement.split(' ')[0]
#         traffic = movement.split(' ')[1]
#
#         if direction_of_travel == 'forward':
#             return f'{self.transport.name} {self.transport.move()} вперед на {traffic} ед.'
#         elif direction_of_travel == 'back':
#             return f'{self.transport.name} {self.transport.move()} назад на {traffic} ед.'
#         elif direction_of_travel == 'left':
#             return f'{self.transport.name} повернул налево на {traffic} градусов.'
#         elif direction_of_travel == 'right':
#             return f'{self.transport.name} повернул направо на {traffic} градусов.'


# =====> test TextDescriptionMove <=====
# print('=========== Движение транспорта =============')
# mover_1 = TextDescriptionMove(transport_1)
# print(mover_1.movement_transport('forward 43'))
# print(mover_1.movement_transport('back 80'))
# print(mover_1.movement_transport('left 70'))
# print(mover_1.movement_transport('right 15'))
# print()

