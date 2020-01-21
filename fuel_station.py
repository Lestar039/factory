from factory import Factory
from fuel import FuelFactory


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
        return FuelFactory().create_fuel(fuel, count_fuel)


class DieselFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки дизеля'

    def add_fuel(self, transport, fuel, count_fuel):
        return FuelFactory().create_fuel(fuel, count_fuel)


class ElectricFuelingStation(AbstractFuelingStation):
    _name = 'Станция для зарядки батарей'

    def add_fuel(self, transport, fuel, count_fuel):
        return FuelFactory().create_fuel(fuel, count_fuel)


class HydrogenFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки водорода'

    def add_fuel(self, transport, fuel, count_fuel):
        return FuelFactory().create_fuel(fuel, count_fuel)


class UraniumFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки урана'

    def add_fuel(self, transport, fuel, count_fuel):
        return FuelFactory().create_fuel(fuel, count_fuel)


class AntimatterFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки антиматерии'

    def add_fuel(self, transport, fuel, count_fuel):
        return FuelFactory().create_fuel(fuel, count_fuel)


class FuelingStation:
    """
    Заправка транспорта
    """

    def add_fuel(self, transport, fuel, count_fuel):
        if fuel == 'Бензин':
            return PetrolFuelingStation().add_fuel(transport, fuel, count_fuel)
        elif fuel == 'Дизель':
            return DieselFuelingStation().add_fuel(transport, fuel, count_fuel)
        elif fuel == 'Электричество':
            return ElectricFuelingStation().add_fuel(transport, fuel, count_fuel)
        elif fuel == 'Водород':
            return HydrogenFuelingStation().add_fuel(transport, fuel, count_fuel)
        elif fuel == 'Уран':
            return UraniumFuelingStation().add_fuel(transport, fuel, count_fuel)
        elif fuel == 'Антиматерия':
            return AntimatterFuelingStation().add_fuel(transport, fuel, count_fuel)
        else:
            return 'ERROR: not correct fueling station!'


if __name__ == "__main__":
    print('=========== Создание транспорта =============')
    transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
    print()
    print('=========== Заправка транспорта =============')
    station_1 = FuelingStation().add_fuel(transport_1, 'Антиматерия', 400)
