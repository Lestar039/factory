from factory import Factory


# =====> Виды заправочных станций <=====
class AbstractFuelingStation:

    def __init__(self, transport, count_fuel):
        self.transport = transport
        self.count_fuel = count_fuel

    def add_fuel(self):
        raise NotImplementedError('Мы тут - AbstractFuelingStation')

    def __str__(self):
        return self.add_fuel()


class PetrolFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки бензина'

    def add_fuel(self):
        return 'Заправляем бензин'


class DieselFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки дизеля'

    def add_fuel(self):
        return 'Заправляем дизель'


class ElectricFuelingStation(AbstractFuelingStation):
    _name = 'Станция для зарядки батарей'

    def add_fuel(self):
        return 'Заряжаем батареи'


class HydrogenFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки водорода'

    def add_fuel(self):
        return 'Заправляем водород'


class UraniumFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки урана'

    def add_fuel(self):
        return 'Заправляем уран'


class AntimatterFuelingStation(AbstractFuelingStation):
    _name = 'Станция для заправки антиматерии'

    def add_fuel(self):
        return 'Заправляем антиматерию'


# =====> Заправленный транспорт <=====
class AbstractRefuelingTransport:

    def __init__(self, transport, count_fuel):
        self.transport = transport
        self.count_fuel = count_fuel

    def refuel(self):
        raise NotImplementedError('Мы тут - AbstractRefuelingTransport')


class PetrolRefuelingTransport(AbstractRefuelingTransport):
    def refuel(self):
        return PetrolFuelingStation(self.transport, self.count_fuel)


class DieselRefuelingTransport(AbstractRefuelingTransport):
    def refuel(self):
        return DieselFuelingStation(self.transport, self.count_fuel)


class ElectricRefuelingTransport(AbstractRefuelingTransport):
    def refuel(self):
        return ElectricFuelingStation(self.transport, self.count_fuel)


class HydrogenRefuelingTransport(AbstractRefuelingTransport):
    def refuel(self):
        return HydrogenFuelingStation(self.transport, self.count_fuel)


class UraniumRefuelingTransport(AbstractRefuelingTransport):
    def refuel(self):
        return UraniumFuelingStation(self.transport, self.count_fuel)


class AntimatterRefuelingTransport(AbstractRefuelingTransport):
    def refuel(self):
        return PetrolFuelingStation(self.transport, self.count_fuel)


# =====> Выбор заправочной станции <=====
class FuelStation(AbstractFuelingStation):
    """
    Выбор заправочной станции в зависимости от типа топлива
    """

    def add_fuel(self):
        if self.transport.fuel_type._name == 'Бензин':
            print(f'{self.transport.name} заправлен  {self.count_fuel} ед. {self.transport.fuel_type._name}')
            return PetrolRefuelingTransport(self.transport, self.count_fuel).refuel()
        elif self.transport.fuel_type._name == 'Дизель':
            print(f'{self.transport.name} заправлен  {self.count_fuel} ед. {self.transport.fuel_type._name}')
            return DieselRefuelingTransport(self.transport, self.count_fuel).refuel()
        elif self.transport.fuel_type._name == 'Электричество':
            print(f'{self.transport.name} заправлен  {self.count_fuel} ед. {self.transport.fuel_type._name}')
            return ElectricRefuelingTransport(self.transport, self.count_fuel).refuel()
        elif self.transport.fuel_type._name == 'Водород':
            print(f'{self.transport.name} заправлен  {self.count_fuel} ед. {self.transport.fuel_type._name}')
            return HydrogenRefuelingTransport(self.transport, self.count_fuel).refuel()
        elif self.transport.fuel_type._name == 'Уран':
            print(f'{self.transport.name} заправлен  {self.count_fuel} ед. {self.transport.fuel_type._name}')
            return UraniumRefuelingTransport(self.transport, self.count_fuel).refuel()
        elif self.transport.fuel_type._name == 'Антиматерия':
            print(f'{self.transport.name} заправлен  {self.count_fuel} ед. {self.transport.fuel_type._name}')
            return AntimatterRefuelingTransport(self.transport, self.count_fuel).refuel()
        else:
            return 'Такой заправки не существует'


# =====> test <=====
# print('=========== Создание транспорта =============')
# transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
# print()
# print('=========== Заправка транспорта =============')
# station_1 = FuelStation(transport_1, 400).add_fuel()
