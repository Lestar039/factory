from fuel import PetrolFuelFactory, DieselFuelFactory, BatteryFuelFactory, \
    HydrogenFuelFactory, UranusFuelFactory, AntimatterFuelFactory
from factory import Factory


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


# station_1 = Station('Бензин').type_station()
# station_2 = Station('Уран').type_station()


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
print('=========== Создание транспорта =============')
transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)

# print('=========== Заправка транспорта =============')
# fuel_1 = FuelingStation(transport_1, 'Антиматерия', 400).fueling()
# print()
