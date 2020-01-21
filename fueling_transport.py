from factory import Factory
from fuel import FuelFactory
from fuel_station import FuelingStation


# =====> Абстрактный заправленный транспорт <=====
class AbstractFuelingTransport:
    """
    Абстрактный заправленный транспорт
    """
    _name = 'Абстрактный транспорт заправлен'

    def fueling(self, transport, fuel, station):
        raise NotImplementedError('Мы тут - AbstractFuelingTransport')

    def __str__(self):
        return self._name


class FuelingTransport(AbstractFuelingTransport):
    """
    Конкретный заправленный транспорт
    """
    _name = 'Транспорт заправлен'

    def fueling(self, transport, fuel, station):
        return 'Транспорт заправлен'


class AbstractFuelingTransportFactory:
    """
    Абстрактный завод заправленных транспортов
    """

    def create_fueling(self, transport, fuel, station):
        raise NotImplementedError('Мы тут - AbstractFuelingTransportFactory')


class FuelingTransportFactory(AbstractFuelingTransportFactory):
    """
    Конкретный завод заправленных транспортов
    """

    def create_fueling(self, transport, fuel, station):
        return FuelingTransport()


# =====> Заправка топливом ТС <=====
class Fueling:
    """
    Заправка транспорта
    """

    def fueling_transport(self, transport, count_fuel):
        create_fuel = FuelFactory().create_fuel(transport.fuel_type, count_fuel)
        use_station = FuelingStation().create_station(transport.fuel_type)
        full_transport = FuelingTransportFactory().create_fueling(transport, create_fuel, use_station)
        return full_transport


if __name__ == "__main__":
    print('=========== Создание транспорта =============')
    transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
    print()
    print('=========== Заправка транспорта =============')
    full_transport_1 = Fueling().fueling_transport(transport_1, 500)
    print(full_transport_1)
