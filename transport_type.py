# ====> Тип танспортного средства <=====
class AbstractTransport:
    _name = 'abstract_type_transport'

    def __init__(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        self.name = name
        self.type_transport = type_transport
        self.engine = engine
        self.mover = mover
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

    def move(self):
        raise NotImplementedError

    def __str__(self):
        return self._name


class GroundTransport(AbstractTransport):
    _name = 'Наземный транспорт'

    def move(self):
        return 'едет'


class WaterTransport(AbstractTransport):
    _name = 'Водный транспорт'

    def move(self):
        return 'плывет'


class AirTransport(AbstractTransport):
    _name = 'Воздушный транспорт'

    def move(self):
        return 'летит'


class AbstractTransportFactory:

    def create_transport(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        raise NotImplementedError


class GroundTransportFactory(AbstractTransportFactory):
    """
    Завод наземного транспорта
    """

    def create_transport(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        return GroundTransport(name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed)


class WaterTransportFactory(AbstractTransportFactory):
    """
    Завод водного транспорта
    """

    def create_transport(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        return WaterTransport(name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed)


class AirTransportFactory(AbstractTransportFactory):
    """
    Завод воздушного транспорта
    """

    def create_transport(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        return AirTransport(name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed)


class TransportFactory:
    """
    Завод различных типов ТС
    """

    def create_transport(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        if type_transport == 'Наземное':
            return GroundTransportFactory().create_transport(
                name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed)
        elif type_transport == 'Водное':
            return WaterTransportFactory().create_transport(
                name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed)
        elif type_transport == 'Воздушное':
            return AirTransportFactory().create_transport(
                name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed)


# =====> test TransportFactory <=====
# tr_1 = TransportFactory().create_transport('Катер', 'Водное', 'Пошневой', 'Винт', 'Дизель', 2, 80)
# print(tr_1)
