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

    def create_engine(self, engine):
        if engine == 'Поршневой':
            return 'Создан поршневой двигатель'
        elif engine == 'Роторный':
            return 'Создан роторный двигатель'
        elif engine == 'Реактивный':
            return 'Создан реактивный двигатель'


class MoverFactory(AbstractMover):
    def create_mover(self, factory):
        if factory == 'Колесо':
            return 'Создано колесо'
        elif factory == 'Гусеница':
            return 'Создана гусеница'
        elif factory == 'Винт':
            return 'Создан винт'
        elif factory == 'Реактивное сопло':
            return 'Создано реактивное сопло'


class FuelFactory(AbstractFuel):
    def create_fuel(self, factory):
        if factory == 'Бензин':
            return 'Создан бензин'
        elif factory == 'Дизель':
            return 'Создано дизельное топливо'
        elif factory == 'Электричество':
            return 'Создан аккумулятор'
        elif factory == 'Водород':
            return 'Создано водородное топливо'
        elif factory == 'Уран':
            return 'Создано урановое топливо'
        elif factory == 'Антиматерия':
            return 'Создана антиматерия'


class Factory:

    def create_engine(self, engine):
        return EngineFactory.create_engine(self, engine)

    def create_mover(self, mover):
        return MoverFactory.create_mover(self, mover)

    def create_fuel(self, fuel):
        return FuelFactory.create_fuel(self, fuel)


b = Factory()
print(b.create_engine('Поршневой'))
print(b.create_mover('Винт'))
print((b.create_fuel('Антиматерия')))


