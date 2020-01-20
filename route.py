from factory import Factory
from move_description import TextDescriptionMove
from driver import CreateDriver
from fuel_station import FuelStation

import time


class Route:
    """
    Отчет пилота о пройденом пути
    """

    def __init__(self, driver):
        self.driver = driver

    def route(self, transport, fuel, movement):
        print(TextDescriptionMove(transport).movement_transport(movement))

        count_move = 1
        for move in transport.mover:
            print(f'{move._name} №{count_move}: пройдено X ед.')
            count_move += 1

        count_engine = 1
        for move in transport.engine:
            print(f'{move._name} №{count_engine}: пройдено X ед.')
            count_engine += 1

        # print(f'Израсходовано {FuelingTransport(transport, 400).fueling()} ед. {transport.fuel_type._name}')
        print(f'Израсходовано {fuel.count_fuel} ед. {transport.fuel_type._name}')

        print('')
        time.sleep(1)

    def start(self):
        pass


# =====> Запуск программы <=====
print('=========== Создание транспорта =============')
transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
print()
print('=========== Заправка транспорта =============')
fuel_1 = FuelStation(transport_1, 400).add_fuel()
print()
print('============ Создание водителя ==============')
driver_1 = CreateDriver(transport_1, 'Dart Weider').create_driver()
print()
print('========= Отчет водителя о маршруте =========')
route_1 = Route(driver_1)
route_1.route(transport_1, fuel_1, 'forward 43')
# route_1.route(transport_1, 'back 80')
# route_1.route(transport_1, 'left 70')
# route_1.route(transport_1, 'right 15')
