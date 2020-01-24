# =====> Создание маршрута движения <=====
class DistanceDirection:
    Forward = 'forward'
    Backward = 'backward'


class RotationDirection:
    Left = 'left'
    Right = 'right'


class DistanceMove:

    def __init__(self, direction, distance):
        self.distance = distance
        self.direction = direction


class RotateMove:

    def __init__(self, direction, rotate):
        self.rotate = rotate
        self.direction = direction


class DescriptionMove:
    """
    Направление движения
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
    Защбивает список на движение и дистанцию
    """

    def create_route(self, command_list):
        new_commands = []
        for command in command_list:
            direction_of_travel = command.split(' ')[0]
            traffic = command.split(' ')[1]
            new_commands.append(DescriptionMove().command(direction_of_travel, traffic))
        return new_commands


class Route:
    """
    Извлекает 1-й элемент из списка команд
    """

    def __init__(self, command_moving):
        self.command_moving = command_moving

    def make_move(self):
        while len(self.command_moving) > 0:
            return self.command_moving.pop(0)
        else:
            return 'Приехали'


if __name__ == "__main__":
    command = ['forward 100', 'backward 300', 'left 30', 'right 40', 'forward 160']
    create_1 = CreateRoute().create_route(command)
    route_1 = Route(create_1).make_move()
