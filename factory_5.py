class AbstractFactory:
    def create_engine(self):
        pass

    def create_mover(self):
        pass


class EngineFactory(AbstractFactory):
    def create_engine(self):
        return 'create engine'


class PistonFactory(EngineFactory):
    """
    Завод поршневых двигателей
    """
    def create_engine(self):
        return 'Создан поршеневой двигатель'


class RotorFactory(EngineFactory):
    """
    Завод роторных двигателей
    """
    def create_engine(self):
        return 'Создан роторный двигатель'


class ReactiveEngineFactory(EngineFactory):
    """
    Завод реактивных двигателей
    """
    def create_engine(self):
        return 'Создан реактивный двигатель'


class MoverFactory(AbstractFactory):
    def create_mover(self):
        return 'create mover'


class WheelsFactory(MoverFactory):
    """
    Завод колес
    """
    def create_mover(self):
        return 'Создано колесо'


class TrackFactory(MoverFactory):
    """
    Завод гусениц
    """
    def create_mover(self):
        return 'Создана гусеница'


class ScrewFactory(MoverFactory):
    """
    Завод винтов
    """
    def create_mover(self):
        return 'Создан винт'


class ReactiveMoverFactory(MoverFactory):
    """
    Завод реактивных сопл
    """
    def create_mover(self):
        return 'Создано реактивное сопло'


class Route:
    """
    Сборка деталей
    """
    def route(self, engine, engine_number, mover, mover_number):
        my_dict = {
            'EngineFactory': [PistonFactory, RotorFactory, ReactiveEngineFactory],
            'MoverFactory': [WheelsFactory, TrackFactory, ScrewFactory, ReactiveMoverFactory]
        }

        if engine == 'Поршневой':
            engine = my_dict['EngineFactory'][0].create_engine(self)
        elif engine == 'Роторный':
            engine = my_dict['EngineFactory'][1].create_engine(self)
        elif engine == 'Реактивный':
            engine = my_dict['EngineFactory'][2].create_engine(self)

        if mover == 'Колесо':
            mover = my_dict['MoverFactory'][0].create_mover(self)
        elif mover == 'Гусеница':
            mover = my_dict['MoverFactory'][1].create_mover(self)
        elif mover == 'Винт':
            mover = my_dict['MoverFactory'][1].create_mover(self)
        elif mover == 'Реактивное сопло':
            mover = my_dict['MoverFactory'][1].create_mover(self)

        total_engine = []
        for engi in range(engine_number):
            total_engine.append(engine)
        total_mover = []
        for mov in range(mover_number):
            total_mover.append(mover)

        return total_engine, total_mover


class Client:
    """
    Заказчик транспорта
    """
    def __init__(self, engine, engine_number, mover, mover_number):
        self.engine = engine
        self.mover = mover
        self.engine_number = engine_number
        self.mover_number = mover_number

    def construction(self):
        transport = Route.route(
            self, self.engine, self.engine_number, self.mover, self.mover_number
        )
        for i in transport:
            print(i)
        print('-----------------------------')
        print('Создано транспортное средство')
        print(f'Двигатель: {self.engine} - {self.engine_number} шт.')
        print(f'Движитель: {self.mover} - {self.mover_number} шт.')


transport_1 = Client('Роторный', 2, 'Гусеница', 6)
transport_1.construction()
