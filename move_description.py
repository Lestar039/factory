from factory import Factory


# =====> Абстрактное движение <=====
class AbstractMove:
    _name = 'абстрактное движение'

    def movement(self, distance):
        raise NotImplementedError('Мы тут - AbstractMove')

    def __str__(self):
        return self._name


# =====> Абстрактный поворот <=====
class AbstractRotate:
    _name = 'абстрактный поворот'

    def make_rotate(self, rotate):
        raise NotImplementedError('Мы тут - AbstractRotate')

    def __str__(self):
        return self._name


# =====> Направление движения <=====
class ForwardMove(AbstractMove):
    _name = 'вперед'

    def movement(self, distance):
        return f'Движется вперед {distance} ед.'


class BackwardMove(AbstractMove):
    _name = 'назад'

    def movement(self, distance):
        return f'Движется вперед {distance} ед.'


# =====> Направление поворота <=====
class LeftRotate(AbstractRotate):
    _name = 'поворот налево'

    def make_rotate(self, rotate):
        return f'Поворачивает налево на {rotate} градусов.'


class RightRotate(AbstractRotate):
    _name = 'поворот направо'

    def make_rotate(self, rotate):
        return f'Поворачивает направо на {rotate} градусов.'


class DescriptionMove:
    """
    Конкретная команда двигаться
    """

    def movement(self, movement, traffic):

        if movement == 'forward':
            return ForwardMove().movement(traffic)
        elif movement == 'backward':
            return BackwardMove().movement(traffic)
        elif movement == 'left':
            return LeftRotate().make_rotate(traffic)
        elif movement == 'right':
            return RightRotate().make_rotate(traffic)
        else:
            return 'ERROR: transport not moving'


class Route:
    input_move: list

    def __init__(self, command_moving):
        self.input_move = command_moving

    def make_move(self):
        while len(self.input_move) != 0:
            if len(self.input_move) > 0:
                print(self.input_move.pop(0))
            else:
                print('Приехали')


class TranslateMoveCommand:
    new_command_list = []

    def translate_command(self, movement: list):
        for command in movement:
            direction_of_travel = command.split(' ')[0]
            traffic = command.split(' ')[1]
            new_direction = DescriptionMove().movement(direction_of_travel, traffic)
            TranslateMoveCommand().new_command_list.append(new_direction)
        return TranslateMoveCommand().new_command_list


if __name__ == "__main__":
    command_to_moving = ['forward 10', 'backward 20', 'left 30', 'right 40']
    command_handler = TranslateMoveCommand()
    route_1 = Route(TranslateMoveCommand().translate_command(command_to_moving))
    route_1.make_move()
