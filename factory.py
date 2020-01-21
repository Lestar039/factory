from engine import EngineFactory
from mover import MoverFactory
from fuel import FuelFactory
from transport_type import TransportFactory


class Factory:
    """
    Завод по сборке транспортных средств
    """

    def create(
            self, name, type_transport, engine, count_engine, mover,
            count_mover, fuel_type, fuel_consumption, transport_speed
    ):
        engine_list = []
        for one_engine in range(count_engine):
            engine_list.append(EngineFactory().create_engine(engine))

        mover_list = []
        for one_mover in range(count_mover):
            mover_list.append(MoverFactory().create_mover(mover))

        new_fuel_type = FuelFactory().create_fuel(fuel_type)

        new_transport = TransportFactory().create_transport(
            name, type_transport, engine_list, mover_list, new_fuel_type,fuel_consumption, transport_speed)

        print(f'Создано ТС: {name}')

        return new_transport


# =====> test Factory <=====
# print('=========== Создание транспорта =============')
# transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
