# ====> Тип танспортного средства <=====
class AbstractTransport:
    _name = 'абстрактный тип ТС'
    distance: float

    def __init__(self, name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed):
        self.name = name
        self.type_transport = type_transport
        self.engines = engines
        self.movers = movers
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

    def move(self, distance):

        if self.fuel.total > 0:
            print(self.fuel.burn(self.fuel_consumption))
        else:
            print('Закончилось топливо')

        for engine in self.engines:
            result = self.distance / self.fuel_consumption
            print(engine.work(result))

        for mover in self.movers:
            print(mover.move())

    def __str__(self):
        return self._name


class GroundTransport(AbstractTransport):
    _name = 'Наземный транспорт'

    def move(self, distance):
        super().move(distance)

    def move_type(self):
        return 'едет'


class WaterTransport(AbstractTransport):
    _name = 'Водный транспорт'

    def move(self, distance):
        super().move(distance)

    def move_type(self):
        return 'плывет'

class AirTransport(AbstractTransport):
    _name = 'Воздушный транспорт'

    def move(self, distance):
        super().move(distance)

    def move_type(self):
        return 'летит'


# =====> Типы заводов транспорта <=====
class AbstractTransportFactory:
    """
    Абстрактный завод ТС
    """

    def create_transport(self, name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed):
        raise NotImplementedError


class GroundTransportFactory(AbstractTransportFactory):
    """
    Завод наземного транспорта
    """

    def create_transport(self, name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed):
        return GroundTransport(name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed)


class WaterTransportFactory(AbstractTransportFactory):
    """
    Завод водного транспорта
    """

    def create_transport(self, name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed):
        return WaterTransport(name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed)


class AirTransportFactory(AbstractTransportFactory):
    """
    Завод воздушного транспорта
    """

    def create_transport(self, name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed):
        return AirTransport(name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed)


class TransportFactory:
    """
    Конкретный завод ТС
    """

    def create_transport(self, name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed):
        if type_transport == 'Наземное':
            print(f'Создано: {type_transport} транспортное средство')
            return GroundTransportFactory().create_transport(
                name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed)
        elif type_transport == 'Водное':
            print(f'Создано: {type_transport} транспортное средство')
            return WaterTransportFactory().create_transport(
                name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed)
        elif type_transport == 'Воздушное':
            print(f'Создано: {type_transport} транспортное средство')
            return AirTransportFactory().create_transport(
                name, type_transport, engines, movers, fuel, fuel_consumption, transport_speed)


if __name__ == "__main__":
    tr_1 = TransportFactory().create_transport('Катер', 'Водное', 'Пошневой', 'Винт', 'Дизель', 2, 80)
