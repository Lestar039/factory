from factory import Factory


# =====> Виды заправочных станций <=====
class AbstractFuelingStation:
    _name = 'abstract_fueling_station'

    def add_fuel(self, transport, count_fuel):
        raise NotImplementedError('Мы тут - AbstractFuelingStation')

    def __str__(self):
        return self._name


class PetrolFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки бензина'

    def add_fuel(self, transport, count_fuel):
        return 'Заправляем бензин'


class DieselFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки дизеля'

    def add_fuel(self, transport, count_fuel):
        return 'Заправляем дизель'


class ElectricFuelingStation(AbstractFuelingStation):
    _name = 'Станция для зарядки батарей'

    def add_fuel(self, transport, count_fuel):
        return 'Заряжаем батареи'


class HydrogenFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки водорода'

    def add_fuel(self, transport, count_fuel):
        return 'Заправляем водород'


class UraniumFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки урана'

    def add_fuel(self, transport, count_fuel):
        return 'Заправляем уран'


class AntimatterFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки антиматерии'

    def add_fuel(self, transport, count_fuel):
        return 'Заправляем антиматерию'


# =====> Заводы заправочных станций <=====
class AbstractStationFactory:
    def create_station(self):
        raise NotImplementedError('Мы тут - AbstractStationFactory')


class PetrolStationFactory(AbstractStationFactory):
    """
    Создаем заправочную станцию бензина
    """

    def create_station(self):
        return PetrolFuelingStation()


class DieselStationFactory(AbstractStationFactory):
    """
    Создаем заправочную станцию дизеля
    """

    def create_station(self):
        return DieselFuelingStation()


class ElectricStationFactory(AbstractStationFactory):
    """
    Создаем заправочную станцию электричества
    """

    def create_station(self):
        return ElectricFuelingStation()


class HydrogenStationFactory(AbstractStationFactory):
    """
    Создаем заправочную станцию водорода
    """

    def create_station(self):
        return HydrogenFuelingStation()


class UraniumStationFactory(AbstractStationFactory):
    """
    Создаем заправочную станцию урана
    """

    def create_station(self):
        return UraniumFuelingStation()


class AntimatterStationFactory(AbstractStationFactory):
    """
    Создаем заправочную станцию антиматерии
    """

    def create_station(self):
        return AntimatterFuelingStation()


# =====> Создание заправочной станции <=====
class FuelingStation:

    def create_station(self, fueling_type):
        if fueling_type == 'Бензин':
            return PetrolStationFactory().create_station()
        elif fueling_type == 'Дизель':
            return DieselStationFactory().create_station()
        elif fueling_type == 'Электричество':
            return ElectricStationFactory().create_station()
        elif fueling_type == 'Водород':
            return HydrogenStationFactory().create_station()
        elif fueling_type == 'Уран':
            return UraniumStationFactory().create_station()
        elif fueling_type == 'Антиматерия':
            return AntimatterStationFactory().create_station()
        else:
            return 'ERROR: not correct fueling station!'


# =====> Заправка транспорта <=====
class RefuelingTransport:
    """
    Заправляем транспорт
    """

    def refueling(self, transport, count_fuel):
        print(f'{transport.name} заправлен {count_fuel} ед. {transport.fuel_type}')
        return FuelingStation().create_station(transport.fuel_type).add_fuel(transport, count_fuel)


# =====> test <=====
print('======= Создание заправочной станции ========')
station_1 = FuelingStation().create_station('Антиматерия')
print(station_1)
print()
print('=========== Создание транспорта =============')
transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
print()
print('=========== Заправка транспорта =============')
refueling_1 = RefuelingTransport().refueling(transport_1, 300)
# print(refueling_1)
