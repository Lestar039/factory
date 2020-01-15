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


# =====> Заправка ТС топливом <=====
class AbstractFuelingStation:
    def add_fuel(self):
        raise NotImplementedError


class PetrolFuelingStation(AbstractFuelingStation):
    def add_fuel(self):
        petrol_fuel = PetrolFuelFactory().create_fuel()
        print('Транспорт заправлен бензином')
        return petrol_fuel


class DieselFuelingStation(AbstractFuelingStation):
    def add_fuel(self):
        diesel_fuel = DieselFuelFactory().create_fuel()
        print('Транспорт заправлен дизелем')
        return diesel_fuel


class ElectricFuelingStation(AbstractFuelingStation):
    def add_fuel(self):
        electric_fuel = BatteryFuelFactory().create_fuel()
        print('Батареи транспорта заряжены')
        return electric_fuel


class HydrogenFuelingStation(AbstractFuelingStation):
    def add_fuel(self):
        hydrogen_fuel = HydrogenFuelFactory().create_fuel()
        print('Транспорт заправлен водородом')
        return hydrogen_fuel


class UraniumFuelingStation(AbstractFuelingStation):
    def add_fuel(self):
        uranium_fuel = UranusFuelFactory().create_fuel()
        print('Транспорт заправлен ураном')
        return uranium_fuel


class AntimatterFuelingStation(AbstractFuelingStation):
    def add_fuel(self):
        antimatter_fuel = AntimatterFuelFactory().create_fuel()
        print('Транспорт заправлен антиматерией')
        return antimatter_fuel


class Station:

    def __init__(self, type_fuel):
        self.type_fuel = type_fuel

    def type_station(self):
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
            return AbstractFuelingStation().add_fuel()


# =====> test Fuel Station <=====
# station_1 = Station('Бензин')
# print(station_1.type_station())


class FuelingStation:
    """
    Заправляем ТС топливом
    """

    def __init__(self, transport, fuel_type, count_fuel):
        self.transport = transport
        self.fuel_type = fuel_type
        self.count_fuel = count_fuel

    def fueling(self):
        new_fuel = Station(self.fuel_type).type_station()
        print(f'{self.transport.name} заправлен топливом: {self.fuel_type} - {self.count_fuel} ед.')
        return new_fuel


# =====> test Fuel <=====
# print('=========== Заправка транспорта =============')
# fuel_1 = FuelingStation(transport_1, 'Антиматерия', 400).fueling()
# print(fuel_1.fueling())
# fuel_1.fueling()
# print()
# print(fuel_1.fueling())

# class SpendFuel:
#     """
#     Расход топлива
#     """
#
#     count = 0
#
#     def spend_fuel(self, transport, count_fuel):
#         SpendFuel.count = count_fuel
#         spend_per_sec = count_fuel - transport.fuel_consumption
#         if spend_per_sec > 0:
#             print(f'Потрачено {transport.fuel_consumption} ед. топлива')
#             return transport.fuel_consumption
#         else:
#             print('Закончилось топливо')


# =====> test SpendFuel < =====
# spend = SpendFuel()
# spend.spend_fuel(transport_1, fuel_1)


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


# class Driver:
#     """
#     Класс пилота
#     """
#
#     def __init__(self, name, transport):
#         self.name = name
#         self.transport = transport
#         print('Создан пилот:', self.name)
#
#     def moving(self, move):
#         return TextDescriptionMove(self.transport).movement_transport(move)
#
#     def start(self):
#         pass

# =====> test Driver  <=====
# print('============= Создание пилота ===============')
# driver_1 = Driver('Shumaher', transport_1)
# print(driver_1.moving('forward 78'))
# driver_1.moving('back 20')
# driver_1.moving('left 45')
# print()
