# =====> Создание маршрута движения <=====
class DistanceDirection:
    """
    Команды движения
    """
    Forward = 'forward'
    Backward = 'backward'


class RotationDirection:
    """
    Команды поворота
    """
    Left = 'left'
    Right = 'right'


class DistanceMove:
    """
    Создание движения
    """

    def __init__(self, direction, distance):
        self.distance = distance
        self.direction = direction


class RotateMove:
    """
    Создание поворота
    """

    def __init__(self, direction, rotate):
        self.rotate = rotate
        self.direction = direction


class DescriptionMove:
    """
    Выбор направления движения
    """

    def command(self, movement, value):
        if movement == 'forward':
            return DistanceMove(distance=value, direction=DistanceDirection.Forward)
        elif movement == 'backward':
            return DistanceMove(distance=value, direction=DistanceDirection.Backward)
        elif movement == 'left':
            return RotateMove(rotate=value, direction=RotationDirection.Left)
        elif movement == 'right':
            return RotateMove(rotate=value, direction=RotationDirection.Right)
        else:
            print('ERROR: transport not moving')


class CreateRoute:
    """
    Создаем список команд
    """

    def create_route(self, command_list):
        new_commands = []
        for command in command_list:
            direction_of_travel, traffic = command.split()
            new_commands.append(DescriptionMove().command(direction_of_travel, traffic))
        return new_commands


if __name__ == "__main__":
    command = ['forward 100', 'backward 300', 'left 30', 'right 40', 'forward 160']
    create_1 = CreateRoute().create_route(command)
