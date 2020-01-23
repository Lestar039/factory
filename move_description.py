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
        return f'движение вперед {distance} ед.'


class BackwardMove(AbstractMove):
    _name = 'назад'

    def movement(self, distance):
        return f'движение вперед {distance} ед.'


# =====> Направление поворота <=====
class LeftRotate(AbstractRotate):
    _name = 'поворот налево'

    def make_rotate(self, rotate):
        return f'поворот налево на {rotate} градусов.'


class RightRotate(AbstractRotate):
    _name = 'поворот направо'

    def make_rotate(self, rotate):
        return f'поворот направо на {rotate} градусов.'


# =====> Команды создающие движение <=====
# class AbstractCommandFactory:
#     """
#     Абстрактная команда двигаться
#     """
#
#     def command(self):
#         return NotImplementedError('Мы тут - AbstractCommand')
#
#
# # class ForwardCommandFactory(AbstractCommandFactory):
# #     """
# #     Команда двигаться вперед
# #     """
# #
# #     def command(self):
# #         return ForwardMove()
# #
# #
# # class BackCommandFactory(AbstractCommandFactory):
# #     """
# #     Команда двигаться назад
# #     """
# #     def command(self):
# #         return BackMove()
# #
# #
# # class LeftCommandFactory(AbstractCommandFactory):
# #     """
# #     Команда поворачивать налево
# #     """
# #
# #     def command(self):
# #         return LeftMove()
# #
# #
# # class RightCommandFactory(AbstractCommandFactory):
# #     """
# #     Команда поворачивать направо
# #     """
# #
# #     def command(self):
# #         return RightMove()


class DescriptionMove:
    """
    Конкретная команда двигаться
    """

    # разбиваем маршрут на направление и количество единиц(градусов)
    def movement(self, movement, traffic):
        # direction_of_travel = movement.split(' ')[0]
        # traffic = movement.split(' ')[1]

        if movement == 'forward':
            return ForwardMove().movement(traffic)
        elif movement == 'back':
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


class SetMoveCommand:

    def set_command(self, ):
        pass


if __name__ == "__main__":
    move_1 = DescriptionMove()
    # print(move_1.movement('forward', 45))
    # print(move_1.movement('back', 37))
    # print(move_1.movement('left', 89))
    # print(move_1.movement('right', 123))

    route_1 = Route(['forward 10', 'backward 20', 'left 30', 'right 40'])
    route_1.make_move()
    # route_1.make_move()
    # route_1.make_move()
    # route_1.make_move()
    # route_1.make_move()
