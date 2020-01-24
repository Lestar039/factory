from factory import Factory
from driver import CreateDriver
from move_description import CreateRoute, Route


print('=========== Создание транспорта =============')
transport_1 = Factory().create(
    'НЛО', 'Воздушное', 'Реактивный', 3, 'Реактивное сопло', 4, 'Антиматерия', 30, 10, 100)
print()

print('============ Создание водителя ==============')
driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
print()

# ============ Создание маршрута ==============
command = ['forward 100', 'backward 300', 'left 30', 'right 40']
create_1 = CreateRoute().create_route(command)
command_list = Route(create_1)

print('========= Отчет водителя о маршруте =========')
driver_1.set_transport(transport_1)
driver_1.set_command(command_list)
driver_1.motion_report()
