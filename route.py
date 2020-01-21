from factory import Factory
from move_description import DescriptionMove
from driver import CreateDriver
from fuel_station import FuelingStation, RefuelingTransport

import time


class Route:
    """
    Отчет пилота о пройденом пути
    """
    route_length = 0
    total_fuel = 0

    # разбиваем маршрут на направление и количество единиц(градусов)
    def movement_transport(self, driver, transport, fuel,  movement):
        direction_of_travel = movement.split(' ')[0]
        traffic = movement.split(' ')[1]

        print(f'TC {transport.name} {transport.move()} {DescriptionMove().command(direction_of_travel)} {traffic} ед.')

        count_move = 1
        for move in transport.mover:
            print(f'{move._name} №{count_move}: пройдено {traffic} ед.')
            count_move += 1
        #
        count_engine = 1
        for move in transport.engine:
            print(f'{move._name} №{count_engine}: пройдено {traffic} ед.')
            count_engine += 1

        # print(f'Израсходовано {fuel.count_fuel} ед. {transport.fuel_type._name}')

        print('')
        time.sleep(1)

    def start(self):
        pass


if __name__ == "__main__":
    print('=========== Создание транспорта =============')
    transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
    print()
    print('======= Создание заправочной станции ========')
    station_1 = FuelingStation().create_station('Антиматерия')
    print(station_1)
    print()
    print('=========== Заправка транспорта =============')
    refueling_1 = RefuelingTransport().refueling(station_1, transport_1, 300)
    print()
    print('============ Создание водителя ==============')
    driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
    print()
    print('========= Отчет водителя о маршруте =========')
    route_1 = Route()
    route_1.movement_transport(driver_1, transport_1, refueling_1, 'forward 43')
    # route_1.movement_transport(driver_1, transport_1, refueling_1, 'back 80')
    # route_1.movement_transport(driver_1, transport_1, refueling_1, 'left 70')
    # route_1.movement_transport(driver_1, transport_1, refueling_1, 'right 15')
