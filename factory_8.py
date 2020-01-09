class AbstractEngine:
    def create_engine(self):
        raise NotImplementedError


class AbstractMover:
    def create_mover(self):
        raise NotImplementedError


class AbstractFuel:
    def create_fuel(self):
        raise NotImplementedError


class EngineFactory(AbstractEngine):

    def __init__(self, engine):
        self.engine = engine

    def create_engine(self):
        if self.engine == 'Поршневой':
            return 'Создан поршневой двигатель'
        elif self.engine == 'Роторный':
            return 'Создан роторный двигатель'
        elif self.engine == 'Реактивный':
            return 'Создан реактивный двигатель'


class MoverFactory(AbstractMover):

    def __init__(self, mover):
        self.mover = mover

    def create_mover(self):
        if self.mover == 'Колесо':
            return 'Создано колесо'
        elif self.mover == 'Гусеница':
            return 'Создана гусеница'
        elif self.mover == 'Винт':
            return 'Создан винт'
        elif self.mover == 'Реактивное сопло':
            return 'Создано реактивное сопло'


class FuelFactory(AbstractFuel):

    def __init__(self, fuel):
        self.fuel = fuel

    def create_fuel(self):
        if self.fuel == 'Бензин':
            return 'Создан бензин'
        elif self.fuel == 'Дизель':
            return 'Создано дизельное топливо'
        elif self.fuel == 'Электричество':
            return 'Создан аккумулятор'
        elif self.fuel == 'Водород':
            return 'Создано водородное топливо'
        elif self.fuel == 'Уран':
            return 'Создано урановое топливо'
        elif self.fuel == 'Антиматерия':
            return 'Создана антиматерия'


class Factory:
    def __init__(self, engine, mover, fuel):
        self.engine = engine
        self.mover = mover
        self.fuel = fuel

    def create_engine(self):
        return EngineFactory(self.engine).create_engine()

    def create_mover(self):
        return MoverFactory(self.mover).create_mover()

    def create_fuel(self):
        return FuelFactory(self.fuel).create_fuel()


# ==> Test Engine, Mover, Fuel Factories <==
# engine_1 = EngineFactory('Роторный')
# print(engine_1.create_engine())
# mover_1 = MoverFactory('Колесо')
# print(mover_1.create_mover())
# fuel_1 = FuelFactory('Бензин')
# print(fuel_1.create_fuel())
# ===========================
transport_1 = Factory('Поршневой', 'Колесо', 'Бензин')
print(transport_1.create_engine())
print(transport_1.create_mover())
print(transport_1.create_fuel())
