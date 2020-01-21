from factory import Factory


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
    _name = 'Станция для заправки бензина'

    def add_fuel(self):
        return PetrolFuelingFuel()


class DieselFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки дизеля'

    def add_fuel(self):
        return DieselFuelingFuel()


class ElectricFuelingStation(AbstractFuelingStation):
    _name = 'Станция для зарядки батарей'

    def add_fuel(self):
        return ElectricFuelingFuel()


class HydrogenFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки водорода'

    def add_fuel(self):
        return HydrogenFuelingFuel()


class UraniumFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки урана'

    def add_fuel(self):
        return UraniumFuelingFuel()


class AntimatterFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки антиматерии'

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
# station_1 = FuelStation('Антиматерия').add_fuel()
# print(station_1.refueling_fuel())



class AbstractFuelingTransport:
    def __init__(self, transport, count_fuel):
        self.transport = transport
        self.count_fuel = count_fuel

    def fueling(self):
        raise NotImplementedError('А теперь мы тут - AbstractFuelingTransport')


class FuelingTransport(AbstractFuelingTransport):
    """
    Заправочная станция
    """

    def fueling(self):
        refueling_transport = (self.transport, FuelStation(self.transport.fuel_type._name).add_fuel(), self.count_fuel)
        print(f'{self.transport.name} заправлен топливом: {self.transport.fuel_type._name} - {self.count_fuel} ед.')
        return refueling_transport


# # =====> test FuelingStation <=====
print('=========== Создание транспорта =============')
transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)

print('=========== Заправка транспорта =============')
fuel_1 = FuelingTransport(transport_1, 400).fueling()
print(type(fuel_1))