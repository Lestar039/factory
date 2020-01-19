from factory import Factory


# =====> Направление движения <=====
class AbastractMove:
    def movement(self):
        raise NotImplementedError('Мы тут - AbastractMove')

    def __str__(self):
        return self.movement()


class ForwardMove(AbastractMove):
    def movement(self):
        return 'вперед'


class BackMove(AbastractMove):
    def movement(self):
        return 'назад'


class LeftMove(AbastractMove):
    def movement(self):
        return 'налево'


class RightMove(AbastractMove):
    def movement(self):
        return 'направо'


# =====> Команды для движения <=====
class AbstractCommand:
    def command(self):
        return NotImplementedError('Мы тут - AbstractCommand')


class ForwardCommand(AbstractCommand):
    def command(self):
        return ForwardMove()


class BackCommand(AbstractCommand):
    def command(self):
        return BackMove()


class LeftCommand(AbstractCommand):
    def command(self):
        return LeftMove()


class RightCommand(AbstractCommand):
    def command(self):
        return RightMove()


class DescriptionMove(AbstractCommand):
    """
    Выбор движения
    """

    def __init__(self, movement):
        self.movement = movement

    def command(self):
        if self.movement == 'forward':
            return ForwardCommand().command()
        elif self.movement == 'back':
            return BackCommand().command()
        elif self.movement == 'left':
            return LeftCommand().command()
        elif self.movement == 'right':
            return RightCommand().command()
        else:
            return 'Не двигается'


# =====> test <=====
# descr_1 = DescriptionMove('forward').command()
# print(descr_1)


class TextDescriptionMove:
    """
    Текстовое описание маршрута
    """

    def __init__(self, transport):
        self.transport = transport

    def movement_transport(self, movement):
        # разбиваем маршрут на направление и количество единиц(градусов)
        direction_of_travel = movement.split(' ')[0]
        traffic = movement.split(' ')[1]

        return f'{self.transport.name} {self.transport.move()} ' \
               f'{DescriptionMove(direction_of_travel).command()} на {traffic} ед.'


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
