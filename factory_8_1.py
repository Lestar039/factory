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
        return 'Бензин сгорает'


class DieselFuel(AbstractFuel):
    __name = 'Дизель'

    def burn(self):
        return 'Дизель сгорает'


class BatteryFuel(AbstractFuel):
    __name = 'Батарея'

    def burn(self):
        return 'Батарея разряжается'


class HydrogenFuel(AbstractFuel):
    __name = 'Водород'

    def burn(self):
        return 'Водород сгорает'


class UraniumFuel(AbstractFuel):
    __name = 'Уран'

    def burn(self):
        return 'Уран распадается'


class AntimatterFuel(AbstractFuel):
    __name = 'Антиматерия'

    def burn(self):
        return 'Антиматерия тратится'


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


# =====> Завод <=====
class Factory:

    def create(
            self, type_transport, engine, count_engine, mover,
            count_mover, fuel, fuel_consumption, transport_speed
    ):
        for count in range(count_engine):
            EngineFactory(engine).create_engine()

        for count in range(count_mover):
            MoverFactory(mover).create_mover()

        FuelFactory(fuel).create_fuel()
        print(f'Создан {type_transport}')
        print(f'Двигатель: {engine} - {count_engine} шт.')
        print(f'Движитель: {mover} - {count_mover} шт.')
        print(f'Расход топлива: {fuel_consumption} единиц на 1 ед. расстояния')
        print(f'Скорость: {transport_speed} ед/ч')

    # def create(
    #         self, type_transport, engine, count_engine, mover,
    #         count_mover, fuel, fuel_consumption, transport_speed
    # ):
    #     transport_list = [type_transport]
    #
    #     for count in range(count_engine):
    #         transport_list.append(EngineFactory(engine).create_engine())
    #
    #     for count in range(count_mover):
    #         transport_list.append(MoverFactory(mover).create_mover())
    #
    #     transport_list.append(FuelFactory(fuel).create_fuel())
    #     transport_list.append(fuel_consumption)
    #     transport_list.append(transport_speed)
    #     return transport_list


# =====> test Factory <=====
Factory().create('Мотоцикл', 'Поршневой', 2, 'Колесо', 2, 'Бензин', 20, 200)
# transport_1 = Factory()
# print(transport_1.create('Мотоцикл', 'Поршневой', 2, 'Колесо', 2, 'Бензин', 20, 200))
print('============================================')


class Fuel:
    """
    Заправляем ТС топливом
    """

    def add_fuel(self, count):
        return f'Транспорт заправлен на {count} ед. топлива'


# =====> test Fuel <=====
# fuel_1 = Fuel()
# print(fuel_1.add_fuel(400))
# print('============================================')


class TextDescriptionMove:
    """
    Текстовое описание маршрута
    """

    def move(self, movement):
        # разбиваем маршрут на направление и количество единиц(градусов)
        direction_of_travel = movement.split(' ')[0]
        traffic = movement.split(' ')[1]

        if direction_of_travel == 'forward':
            print(f'Транспорт продвинулся вперед на {traffic} ед.')
        elif direction_of_travel == 'back':
            print(f'Транспорт продвинулся назад на {traffic} ед.')
        elif direction_of_travel == 'left':
            print(f'Транспорт повернул налево на {traffic} градусов')
        elif direction_of_travel == 'right':
            print(f'Транспорт повернул направо на {traffic} градусов')


# =====> test TextDescriptionMove <=====
# mover_1 = TextDescriptionMove()
# mover_1.move('forward 43')
# mover_1.move('left 70')
# mover_1.move('back 80')
# mover_1.move('right 15')
# print('============================================')


class Driver:
    """
    Класс пилота
    """

    def __init__(self, name):
        self.name = name
        print('Создан пилот', self.name)

    def moving(self, movement):
        return TextDescriptionMove().move(movement)

# =====> test Driver  <=====
# driver_1 = Driver('Shumaher')
# driver_1.moving('forward 78')
# print('============================================')
