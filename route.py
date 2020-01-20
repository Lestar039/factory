from factory import Factory
from move_description import TextDescriptionMove
from driver import CreateDriver
from fuel_station import FuelingTransport

import time


class Route:
    """
    Отчет пилота о пройденом пути
    """

    def __init__(self, driver):
        self.driver = driver

    def route(self, transport, movement):
        print(TextDescriptionMove(transport).movement_transport(movement))

        count_move = 1
        for move in transport.mover:
            print(f'№{count_move} {move}')
            count_move += 1

        count_engine = 1
        for move in transport.engine:
            print(f'№{count_engine} {move}')
            count_engine += 1

        print(f'{transport.fuel_type} ед.')

        print('')
        time.sleep(1)
        # return transport_movement

    def start(self):
        pass


# =====> Запуск программы <=====
print('=========== Создание транспорта =============')
transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
print()
print('============ Создание водителя ==============')
driver_1 = CreateDriver(transport_1, 'Пилот', 'Dart Weider').create_driver()
print()
print('========= Отчет водителя о маршруте =========')
route_1 = Route(driver_1)
route_1.route(transport_1, 'forward 43')
route_1.route(transport_1, 'back 80')
# route_1.route(transport_1, 'left 70')
# route_1.route(transport_1, 'right 15')
