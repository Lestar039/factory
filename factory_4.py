class AbstractFactory:

    def create_engine(self):
        pass

    def create_mover(self):
        pass

    def create_transport(self):
        pass


class EngineFactory(AbstractFactory):
    """
    Создает двигатели
    """
    def create_piston_engine(self):
        pass

    def create_rotor_engine(self):
        pass

    def create_reactive_engine(self):
        pass


class MoverFactory(AbstractFactory):
    """
    Создает движители
    """
    def create_wheel(self):
        pass

    def create_track(self):
        pass

    def create_screw(self):
        pass

    def create_reactive_mover(self):
        pass


class TypeTransportFactory(AbstractFactory):
    """
    Создает различные типы транспорта
    """
    def create_ground_type(self):
        pass

    def create_water_type(self):
        pass

    def create_air_type(self):
        pass


class PistonFactory(EngineFactory):
    """
    Завод поршневых двигателей
    """
    def create_piston_engine(self):
        pass


class RotorFactory(EngineFactory):
    """
    Завод роторных двигателей
    """
    def create_rotor_engine(self):
        pass


class ReactiveEngineFactory(EngineFactory):
    """
    Завод реактивных двигателей
    """
    def create_reactive_engine(self):
        pass


class WheelsFactory(MoverFactory):
    """
    Завод колес
    """
    def create_wheel(self):
        pass


class TrackFactory(MoverFactory):
    """
    Завод гусениц
    """
    def create_track(self):
        pass


class ScrewFactory(MoverFactory):
    """
    Завод винтов
    """
    def create_screw(self):
        pass


class ReactiveMoverFactory(MoverFactory):
    """
    Завод реактивных сопл
    """
    def create_reactive_mover(self):
        pass


class GroundTransportFactory(TypeTransportFactory):
    """
    Завод наземного транспорта
    """
    def create_ground_type(self):
        pass


class WaterTransportFactory(TypeTransportFactory):
    """
    Завод водного транспорта
    """
    def create_water_type(self):
        pass


class AirTransportFactory(TypeTransportFactory):
    """
    Завод воздушного транспорта
    """
    def create_air_type(self):
        pass


class AssembleFactory:
    """
    Собирает транспорт из деталей
    """
    piston_engine = PistonFactory.create_piston_engine
    rotor_engine = RotorFactory.create_rotor_engine
    reactive_engine = ReactiveEngineFactory.create_reactive_engine

    wheels_mover = WheelsFactory.create_wheel
    track_mover = TrackFactory.create_track
    screw_mover = ScrewFactory.create_screw
    reactive_mover = ReactiveMoverFactory.create_reactive_mover

    ground_type = GroundTransportFactory.create_ground_type
    water_type = WaterTransportFactory.create_water_type
    air_type = AirTransportFactory.create_air_type

    def __init__(self, engine, engine_number, mover, mover_number, transport_type):
        self.engine = engine
        self.engine_number = engine_number
        self.mover = mover
        self.mover_number = mover_number
        self.transport_type = transport_type

    def create(self):
        if self.engine == 'Наземный':
            print('Создан', ground_type, 'транспорт')
