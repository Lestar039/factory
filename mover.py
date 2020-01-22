# =====> Движители <=====
class AbstractMover:
    _name = 'абстрактный движетель'

    def move(self):
        raise NotImplementedError

    def __str__(self):
        return self._name


class WheelsMover(AbstractMover):
    _name = 'Колесо'

    def move(self):
        return 'Колесо крутится'


class TrackMover(AbstractMover):
    _name = 'Гусеница'

    def move(self):
        return 'Гусеница крутится'


class ScrewMover(AbstractMover):
    _name = 'Винт'

    def move(self):
        return 'Винт крутится'


class ReactiveMover(AbstractMover):
    _name = 'Реактивное сопло'

    def move(self):
        return 'Реактивное сопло работает'


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
    Роутре фабрик
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
