# =====> Двигатели <=====
class AbstractEngine:
    _name = 'abstract_engine'

    def work(self):
        raise NotImplementedError

    def __str__(self):
        return self._name


class PistonEngine(AbstractEngine):
    _name = 'Поршневой двигатель'

    def work(self):
        return 'Поршневой двигатель работает'


class RotorEngine(AbstractEngine):
    _name = 'Роторный двигатель'

    def work(self):
        return 'Роторный двигатель работает'


class ReactiveEngine(AbstractEngine):
    _name = 'Реактивный двигатель'

    def work(self):
        return 'Реактивный двигатель работает'


# =====> Заводы двигателей <=====
class AbstractEngineFactory:
    def create_engine(self):
        raise NotImplementedError


class PistonFactory(AbstractEngineFactory):
    """
    Завод поршневых двигателей
    """

    def create_engine(self):
        return PistonEngine()


class RotorFactory(AbstractEngineFactory):
    """
    Завод роторных двигателей
    """

    def create_engine(self):
        return RotorEngine()


class ReactiveFactory(AbstractEngineFactory):
    """
    Завод реактивных двигателей
    """

    def create_engine(self):
        return ReactiveEngine()


class EngineFactory:

    def create_engine(self, engine):
        if engine == 'Поршневой':
            return PistonFactory().create_engine()
        elif engine == 'Роторный':
            return RotorFactory().create_engine()
        elif engine == 'Реактивный':
            return ReactiveFactory().create_engine()


# =====> test <=====
# engine_1 = EngineFactory().create_engine('Роторный')
# print(engine_1)
