# =====> Двигатели <=====
class AbstractEngine:
    _name = 'абстрактный двигатель'

    def work(self, consumed_distance):
        return f'{self._name} работает {consumed_distance} ед.'

    def __str__(self):
        return self._name


class PistonEngine(AbstractEngine):
    _name = 'Поршневой двигатель'


class RotorEngine(AbstractEngine):
    _name = 'Роторный двигатель'


class ReactiveEngine(AbstractEngine):
    _name = 'Реактивный двигатель'


# =====> Заводы двигателей <=====
class AbstractEngineFactory:
    """
    Абстрактный завод двигателей
    """

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


class EngineFactoryRouter:
    """
    Роутер фабрик
    """

    def engine_type_router(self, engine_type):
        if engine_type == 'Поршневой':
            return PistonFactory()
        elif engine_type == 'Роторный':
            return RotorFactory()
        elif engine_type == 'Реактивный':
            return ReactiveFactory()


class EngineFactory:
    """
    Конкретный завод двигателей
    """

    def create_engine(self, engine_type):
        engine = EngineFactoryRouter().engine_type_router(engine_type).create_engine()
        print(f'Создан {engine}')
        return engine


if __name__ == "__main__":
    engine_1 = EngineFactory().create_engine('Роторный')
