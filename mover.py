# =====> Движители <=====
class AbstractMover:
    def move(self):
        raise NotImplementedError

    def __str__(self):
        return self.move()


class WheelsMover(AbstractMover):
    __name = 'Колесо'

    def move(self):
        return 'Колесо крутится'


class TrackMover(AbstractMover):
    __name = 'Гусеница'

    def move(self):
        return 'Гусеница крутится'


class ScrewMover(AbstractMover):
    __name = 'Винт'

    def move(self):
        return 'Винт крутится'


class ReactiveMover(AbstractMover):
    __name = 'Реактивное сопло'

    def move(self):
        return 'Реактивное сопло работает'


# =====> Заводы движителей <=====
class AbstractMoverFactory:
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


class MoverFactory(AbstractMoverFactory):

    def __init__(self, mover):
        self.mover = mover

    def create_mover(self):
        if self.mover == 'Колесо':
            return WheelsFactory().create_mover()
        elif self.mover == 'Гусеница':
            return TrackFactory().create_mover()
        elif self.mover == 'Винт':
            return ScrewFactory().create_mover()
        elif self.mover == 'Реактивное сопло':
            return ReactiveMoverFactory().create_mover()
