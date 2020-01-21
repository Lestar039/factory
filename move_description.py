from factory import Factory


# =====> Направление движения <=====
class AbstractMove:
    _name = 'abstract move'

    def movement(self):
        raise NotImplementedError('Мы тут - AbstractMove')

    def __str__(self):
        return self._name


class ForwardMove(AbstractMove):
    _name = 'вперед'

    def movement(self):
        return ' движение вперед'


class BackMove(AbstractMove):
    _name = 'назад'

    def movement(self):
        return 'движение назад'


class LeftMove(AbstractMove):
    _name = 'налево'

    def movement(self):
        return 'поворот налево'


class RightMove(AbstractMove):
    _name = 'направо'

    def movement(self):
        return 'поворот направо'


# =====> Команды создающие движение <=====
class AbstractCommandFactory:
    def command(self):
        return NotImplementedError('Мы тут - AbstractCommand')


class ForwardCommandFactory(AbstractCommandFactory):
    """
    Команда двигаться вперед
    """

    def command(self):
        return ForwardMove()


class BackCommandFactory(AbstractCommandFactory):
    """
    Команда двигаться назад
    """
    def command(self):
        return BackMove()


class LeftCommandFactory(AbstractCommandFactory):
    """
    Команда поворачивать налево
    """

    def command(self):
        return LeftMove()


class RightCommandFactory(AbstractCommandFactory):
    """
    Команда поворачивать направо
    """

    def command(self):
        return RightMove()


class DescriptionMove:
    """
    Выбор движения
    """

    def command(self, movement):
        if movement == 'forward':
            return ForwardCommandFactory().command()
        elif movement == 'back':
            return BackCommandFactory().command()
        elif movement == 'left':
            return LeftCommandFactory().command()
        elif movement == 'right':
            return RightCommandFactory().command()
        else:
            return 'ERROR: transport not moving'


# =====> test <=====
# description_1 = DescriptionMove().command('forward')
# print(description_1)


# class TextDescriptionMove:
#     """
#     Текстовое описание маршрута
#     """
#
#     def __init__(self, transport):
#         self.transport = transport
#
#     def movement_transport(self, movement):
#         # разбиваем маршрут на направление и количество единиц(градусов)
#         direction_of_travel = movement.split(' ')[0]
#         traffic = movement.split(' ')[1]
#
#         return f'{self.transport.name} {self.transport.move()} ' \
#                f'{DescriptionMove(direction_of_travel).command()} на {traffic} ед.'
#

# # =====> test TextDescriptionMove <=====
# print('=========== Создание транспорта =============')
# transport_1 = Factory().create('НЛО', 'Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 2, 90)
#
# print('=========== Движение транспорта =============')
# mover_1 = TextDescriptionMove(transport_1)
# print(mover_1.movement_transport('forward 43'))
# print(mover_1.movement_transport('back 80'))
# print(mover_1.movement_transport('left 70'))
# print(mover_1.movement_transport('right 15'))
