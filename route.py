from factory import Factory
from move_description import DescriptionMove
from driver import CreateDriver

import time

print('=========== Создание транспорта =============')
transport_1 = Factory().create(
    'НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 200, 2, 90)
print('============ Создание водителя ==============')
driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
print('========= Отчет водителя о маршруте =========')
print(driver_1.motion_report(['forward 10', 'backward 20', 'left 30', 'right 40']))
# route_1.movement_transport(driver_1, transport_1, refueling_1, 'forward 43')
# route_1.movement_transport(driver_1, transport_1, refueling_1, 'back 80')
# route_1.movement_transport(driver_1, transport_1, refueling_1, 'left 70')
# route_1.movement_transport(driver_1, transport_1, refueling_1, 'right 15')
