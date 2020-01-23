from factory import Factory
from move_description import TranslateMoveCommand, Route
from driver import CreateDriver


print('=========== Создание транспорта =============')
transport_1 = Factory().create(
    'НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 200, 2, 90)
print()
print('============ Создание водителя ==============')
driver_1 = CreateDriver().create_driver(transport_1, 'Dart Weider')
print()
print('========= Отчет водителя о маршруте =========')
command_to_moving = ['forward 10', 'backward 20', 'left 30', 'right 40']
command_handler = TranslateMoveCommand()
route_1 = Route(command_handler.translate_command(command_to_moving))
route_1.make_move()
