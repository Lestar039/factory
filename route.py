from factory import Factory
from move_description import TranslateMoveCommand, Route
from driver import CreateDriver
from fuel import BurningFuel


print('=========== Создание транспорта =============')
transport_1 = Factory().create(
    'НЛО', 'Воздушное', 'Реактивный', 3, 'Реактивное сопло', 4, 'Антиматерия', 200, 2, 90)
# transport_1.move()
print()
print('============ Создание водителя ==============')
driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
print()
print('========= Отчет водителя о маршруте =========')
command = ['forward 10', 'backward 20', 'left 30', 'right 40']

driver_1.set_transport(transport_1)
driver_1.set_command(command)
driver_1.motion_report()

# print('fuel:')
# burn_1 = BurningFuel()
# burn_1.burning_fuel(transport_1)
