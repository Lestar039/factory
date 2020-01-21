# =====> Направление движения <=====
class AbstractMove:
    _name = 'абстрактное движение'

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
    _name = 'поворот налево'

    def movement(self):
        return 'поворот налево'


class RightMove(AbstractMove):
    _name = 'поворот направо'

    def movement(self):
        return 'поворот направо'


# =====> Команды создающие движение <=====
class AbstractCommandFactory:
    """
    Абстрактная команда двигаться
    """

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
    Конкретная команда двигаться
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


if __name__ == "__main__":
    move_1 = DescriptionMove()
    print(move_1.command('forward'))
    print(move_1.command('back'))
    print(move_1.command('left'))
    print(move_1.command('right'))
