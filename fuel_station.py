# =====> Виды заправочных станций <=====
class AbstractFuelingStation:
    _name = 'абстрактная заправочная станция'

    def add_fuel(self, transport, fuel, count_fuel):
        raise NotImplementedError('Мы тут - AbstractFuelingStation')

    def __str__(self):
        return self._name


class PetrolFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки бензина'

    def add_fuel(self, transport, fuel, count_fuel):
        return 'Заправляем бензин'


class DieselFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки дизеля'

    def add_fuel(self, transport, fuel, count_fuel):
        return 'Заправляем дизель'


class ElectricFuelingStation(AbstractFuelingStation):
    _name = 'Станция для зарядки батарей'

    def add_fuel(self, transport, fuel, count_fuel):
        return 'Заряжаем батареи'


class HydrogenFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки водорода'

    def add_fuel(self, transport, fuel, count_fuel):
        return 'Заправляем водород'


class UraniumFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки урана'

    def add_fuel(self, transport, fuel, count_fuel):
        return 'Заправляем уран'


class AntimatterFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки антиматерии'

    def add_fuel(self, transport, fuel, count_fuel):
        return 'Заправляем антиматерию'


# =====> Фабрики заправочных станций <=====
class AbstractStationFactory:
    """
    Абстрактный завод заправочных станций
    """

    def create_station(self):
        raise NotImplementedError('Мы тут - AbstractStationFactory')


class PetrolStationFactory(AbstractStationFactory):
    """
    Завод заправочной станции бензина
    """

    def create_station(self):
        return PetrolFuelingStation()


class DieselStationFactory(AbstractStationFactory):
    """
    Завод заправочной станции дизеля
    """

    def create_station(self):
        return DieselFuelingStation()


class ElectricStationFactory(AbstractStationFactory):
    """
    Завод заправочной станции электричества
    """

    def create_station(self):
        return ElectricFuelingStation()


class HydrogenStationFactory(AbstractStationFactory):
    """
    Завод заправочной станции водорода
    """

    def create_station(self):
        return HydrogenFuelingStation()


class UraniumStationFactory(AbstractStationFactory):
    """
    Завод заправочной станции урана
    """

    def create_station(self):
        return UraniumFuelingStation()


class AntimatterStationFactory(AbstractStationFactory):
    """
    Завод заправочной станции антиматерии
    """

    def create_station(self):
        return AntimatterFuelingStation()


class FuelingStation:
    """
    Выбор заправочной станции
    """

    def create_station(self, fuel):
        if fuel == 'Бензин':
            return PetrolStationFactory().create_station()
        elif fuel == 'Дизель':
            return DieselStationFactory().create_station()
        elif fuel == 'Электричество':
            return ElectricStationFactory().create_station()
        elif fuel == 'Водород':
            return HydrogenStationFactory().create_station()
        elif fuel == 'Уран':
            return UraniumStationFactory().create_station()
        elif fuel == 'Антиматерия':
            return AntimatterStationFactory().create_station()


if __name__ == "__main__":
    station_1 = FuelingStation().create_station('Электричество')
    print(station_1)

