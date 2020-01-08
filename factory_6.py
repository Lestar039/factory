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
        # return 'Создан роторный двигатель'
        print('Создан роторный двигатель')


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


class Route:
    """
    Сборка деталей
    """

    # def route(self, type_name, engine, engine_number, mover, mover_number,
    #           type_fuel, fuel_consumption, transport_speed):
    #
    #     factory_dict = {
    #         'EngineFactory': [PistonFactory, RotorFactory, ReactiveEngineFactory],
    #         'MoverFactory': [WheelsFactory, TrackFactory, ScrewFactory, ReactiveMoverFactory],
    #         'FuelFactory': [PetrolFuel, DieselFuel, BatteryFuel, HydrogenFuel, UranusFuel, AntimatterFuel]
    #     }
    #
    #     if engine == 'Поршневой':
    #         engine = factory_dict['EngineFactory'][0].create_engine(self)
    #     elif engine == 'Роторный':
    #         engine = factory_dict['EngineFactory'][1].create_engine(self)
    #     elif engine == 'Реактивный':
    #         engine = factory_dict['EngineFactory'][2].create_engine(self)
    #
    #     for engi in range(engine_number):
    #         print(engine)
    #
    #     if mover == 'Колесо':
    #         mover = factory_dict['MoverFactory'][0].create_mover(self)
    #     elif mover == 'Гусеница':
    #         mover = factory_dict['MoverFactory'][1].create_mover(self)
    #     elif mover == 'Винт':
    #         mover = factory_dict['MoverFactory'][1].create_mover(self)
    #     elif mover == 'Реактивное сопло':
    #         mover = factory_dict['MoverFactory'][1].create_mover(self)
    #
    #     for mov in range(mover_number):
    #         print(mover)
    #
    #     if type_fuel == 'Бензин':
    #         # type_fuel = factory_dict['FuelFactory'][0].create_fuel(self)
    #         return PetrolFuel()
    #     elif type_fuel == 'Дизель':
    #         type_fuel = factory_dict['FuelFactory'][1].create_fuel(self)
    #     elif type_fuel == 'Электричество':
    #         type_fuel = factory_dict['FuelFactory'][2].create_fuel(self)
    #     elif type_fuel == 'Водород':
    #         type_fuel = factory_dict['FuelFactory'][3].create_fuel(self)
    #     elif type_fuel == 'Уран':
    #         type_fuel = factory_dict['FuelFactory'][4].create_fuel(self)
    #     elif type_fuel == 'Антиматерия':
    #         type_fuel = factory_dict['FuelFactory'][5].create_fuel(self)
    #
    #     # print(type_fuel)
    #
    #     print('-----------------------------')
    #     print(f'Создано: {type_name} транспортное средство')
    #     print(f'Двигатель: {engine} - {engine_number} шт.')
    #     print(f'Движитель: {mover} - {mover_number} шт.')
    #     print('Тип топлива:', type_fuel)
    #     print(f'Расход топлива: {fuel_consumption} единиц на 1 ед. расстояния')
    #     print(f'Скорость: {transport_speed} ед/ч')
    #
    #     return type_name, engine, engine_number, mover, mover_number, \
    #            type_fuel, fuel_consumption, transport_speed

    def engine(self, engine):

        if engine == 'Поршневой':
            return PistonFactory()
        elif engine == 'Роторный':
            return RotorFactory()
        elif engine == 'Реактивный':
            return ReactiveEngineFactory()

    def mover(self, mover):

        if mover == 'Колесо':
            return WheelsFactory()
        elif mover == 'Гусеница':
            return TrackFactory()
        elif mover == 'Винт':
            return ScrewFactory()
        elif mover == 'Реактивное сопло':
            return ReactiveMoverFactory()

    def fuel(self, type_fuel):

        if type_fuel == 'Бензин':
            return PetrolFuel()
        elif type_fuel == 'Дизель':
            return DieselFuel()
        elif type_fuel == 'Электричество':
            return BatteryFuel()
        elif type_fuel == 'Водород':
            return HydrogenFuel()
        elif type_fuel == 'Уран':
            return UranusFuel()
        elif type_fuel == 'Антиматерия':
            return AntimatterFuel()

    def other_detail(self, type_name, engine, engine_number, mover, mover_number, type_fuel,
                     fuel_consumption, transport_speed):
        print('-----------------------------')
        print(f'Создано: {type_name} транспортное средство')
        print(f'Двигатель: {engine} - {engine_number} шт.')
        print(f'Движитель: {mover} - {mover_number} шт.')
        print('Тип топлива:', type_fuel)
        print(f'Расход топлива: {fuel_consumption} единиц на 1 ед. расстояния')
        print(f'Скорость: {transport_speed} ед/ч')


class Client:
    """
    Заказчик транспорта
    """

    def __init__(
            self, type_name, engine, engine_number, mover, mover_number,
            type_fuel, fuel_consumption, transport_speed):
        self.type_name = type_name
        self.engine = engine
        self.mover = mover
        self.engine_number = engine_number
        self.mover_number = mover_number
        self.type_fuel = type_fuel
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

    # def construction(self):
    #     transport = Route.route(
    #         self, self.type_name, self.engine, self.engine_number, self.mover, self.mover_number,
    #         self.type_fuel, self.fuel_consumption, self.transport_speed
    #     )
    #
    #     return transport

    def construction(self):
        engine_1 = Route.engine(self, self.engine)
        # mover = Route.mover(self, self.mover)
        # other_detail = Route.other_detail(
        #     self, self.type_name, self.engine, self.engine_number, self.mover, self.mover_number,
        #     self.type_fuel, self.fuel_consumption, self.transport_speed)

        # return engine, mover, other_detail
        return engine_1


transport_1 = Client('Наземное', 'Роторный', 3, 'Гусеница', 6, 'Уран', 10, 250)
print(transport_1.construction())
