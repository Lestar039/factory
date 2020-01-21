# =====> Движители <=====
class AbstractMover:
    _name = 'abstract mover'

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


class MoverFactory:

    def create_mover(self, mover):
        if mover == 'Колесо':
            print(f'Создано {mover}')
            return WheelsFactory().create_mover()
        elif mover == 'Гусеница':
            print(f'Создана {mover}')
            return TrackFactory().create_mover()
        elif mover == 'Винт':
            print(f'Создан {mover}')
            return ScrewFactory().create_mover()
        elif mover == 'Реактивное сопло':
            print(f'Создано {mover}')
            return ReactiveMoverFactory().create_mover()


if __name__ == "__main__":
    mover_1 = MoverFactory().create_mover('Винт')
