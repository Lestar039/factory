# ====> Тип танспортного средства <=====
class AbstractTransport:

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

    def __init__(self, name, type_transport, engine, mover, fuel_type, fuel_consumption, transport_speed):
        self.name = name
        self.type_transport = type_transport
        self.engine = engine
        self.mover = mover
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

    def create_transport(self):
        raise NotImplementedError


class GroundTransportFactory(AbstractTransportFactory):
    """
    Завод наземного транспорта
    """

    def create_transport(self):
        return GroundTransport(self.name, self.type_transport, self.engine, self.mover,
                               self.fuel_type, self.fuel_consumption, self.transport_speed)


class WaterTransportFactory(AbstractTransportFactory):
    """
    Завод водного транспорта
    """

    def create_transport(self):
        return WaterTransport(self.name, self.type_transport, self.engine, self.mover,
                              self.fuel_type, self.fuel_consumption, self.transport_speed)


class AirTransportFactory(AbstractTransportFactory):
    """
    Завод воздушного транспорта
    """

    def create_transport(self):
        return AirTransport(self.name, self.type_transport, self.engine, self.mover,
                            self.fuel_type, self.fuel_consumption, self.transport_speed)


class TransportFactory(AbstractTransportFactory):
    """
    Завод различных типов ТС
    """

    def create_transport(self):
        if self.type_transport == 'Наземное':
            return GroundTransportFactory(self.name, self.type_transport, self.engine, self.mover, self.fuel_type,
                                          self.fuel_consumption, self.transport_speed).create_transport()
        elif self.type_transport == 'Водное':
            return WaterTransportFactory(self.name, self.type_transport, self.engine, self.mover, self.fuel_type,
                                         self.fuel_consumption, self.transport_speed).create_transport()
        elif self.type_transport == 'Воздушное':
            return AirTransportFactory(self.name, self.type_transport, self.engine, self.mover, self.fuel_type,
                                       self.fuel_consumption, self.transport_speed).create_transport()


# =====> test TransportFactory <=====
# tr_1 = TransportFactory('Катер', 'Водное', 'Пошневой', 'Винт', 'Дизель', 2, 80).create_transport()
# print(tr_1)
