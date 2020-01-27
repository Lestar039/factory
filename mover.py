# =====> Движители <=====
class AbstractMover:
    _name = 'абстрактный движетель'

    def move(self, move_distance):
        return f'{self._name} работает {move_distance} ед.'

    def __str__(self):
        return self._name


class WheelsMover(AbstractMover):
    _name = 'Колесо'


class TrackMover(AbstractMover):
    _name = 'Гусеница'


class ScrewMover(AbstractMover):
    _name = 'Винт'


class ReactiveMover(AbstractMover):
    _name = 'Реактивное сопло'


# =====> Заводы движителей <=====
class AbstractMoverFactory:
    """
    Абстрактный завод движетелей
    """

    def create_mover(self):
        raise NotImplementedError


class WheelsFactory(AbstractMoverFactory):
    """
    Завод колес
    """

    def create_mover(self):
        return WheelsMover()


class TrackFactory(AbstractMoverFactory):
    """
    Завод гусениц
    """

    def create_mover(self):
        return TrackMover()


class ScrewFactory(AbstractMoverFactory):
    """
    Завод винтов
    """

    def create_mover(self):
        return ScrewMover()


class ReactiveMoverFactory(AbstractMoverFactory):
    """
    Завод реактивных сопл
    """

    def create_mover(self):
        return ReactiveMover()


class MoverFactoryRouter:
    """
    Роутер фабрик
    """

    def mover_type_router(self, mover_type):
        if mover_type == 'Колесо':
            return WheelsFactory()
        elif mover_type == 'Гусеница':
            return TrackFactory()
        elif mover_type == 'Винт':
            return ScrewFactory()
        elif mover_type == 'Реактивное сопло':
            return ReactiveMoverFactory()


class MoverFactory:
    """
    Конкретный завод движетелей
    """

    def create_mover(self, mover_type):
        mover = MoverFactoryRouter().mover_type_router(mover_type).create_mover()
        print(f'Создан {mover}')
        return mover


if __name__ == "__main__":
    mover_1 = MoverFactory().create_mover('Винт')
