# =====> Топливо <=====
class AbstractFuel:
    _name = 'абстрактное топливо'

    def __init__(self, total):
        self.total = total

    def burn(self, consumed_quantity):
        self.total -= consumed_quantity
        return f'Израсходовалось {consumed_quantity} ед. {self._name}'

    def __str__(self):
        return self._name


class PetrolFuel(AbstractFuel):
    _name = 'Бензин'

    def burn(self, consumed_quantity):
        return 'Расходуется бензин'


class DieselFuel(AbstractFuel):
    _name = 'Дизель'

    def burn(self, consumed_quantity):
        return 'Расходуется дизель'


class BatteryFuel(AbstractFuel):
    _name = 'Батарея'

    def burn(self, consumed_quantity):
        return 'Расходуется батарея'


class HydrogenFuel(AbstractFuel):
    _name = 'Водород'

    def burn(self, consumed_quantity):
        return 'Расходуется водород'


class UraniumFuel(AbstractFuel):
    _name = 'Уран'

    def burn(self, consumed_quantity):
        return 'Расходуется уран'


class AntimatterFuel(AbstractFuel):
    _name = 'Антиматерия'

    def burn(self, consumed_quantity):
        return 'Расходуется антиматерия'


# =====> Топливные заводы <=====
class AbstractFuelFactory:
    """
    Абстрактный топливный завод
    """

    def create_fuel(self, count_fuel):
        raise NotImplementedError


class PetrolFuelFactory(AbstractFuelFactory):
    """
    Завод по производству бензина
    """

    def create_fuel(self, count_fuel):
        return PetrolFuel(count_fuel)


class DieselFuelFactory(AbstractFuelFactory):
    """
     Завод по производству дизеля
    """

    def create_fuel(self, count_fuel):
        return DieselFuel(count_fuel)


class BatteryFuelFactory(AbstractFuelFactory):
    """
    Завод по производству аккумуляторов
    """

    def create_fuel(self, count_fuel):
        return BatteryFuel(count_fuel)


class HydrogenFuelFactory(AbstractFuelFactory):
    """
    Завод по производству водорода
    """

    def create_fuel(self, count_fuel):
        return HydrogenFuel(count_fuel)


class UranusFuelFactory(AbstractFuelFactory):
    """
    Завод по производству урана
    """

    def create_fuel(self, count_fuel):
        return UraniumFuel(count_fuel)


class AntimatterFuelFactory(AbstractFuelFactory):
    """
    Завод по производству антиматерии
    """

    def create_fuel(self, count_fuel):
        return AntimatterFuel(count_fuel)


class FuelFactoryRouter:
    """
    Роутре фабрик
    """

    def fuel_type_router(self, fuel_type, count_fuel):
        if fuel_type == 'Бензин':
            return PetrolFuelFactory()
        elif fuel_type == 'Дизель':
            return DieselFuelFactory()
        elif fuel_type == 'Электричество':
            return BatteryFuelFactory()
        elif fuel_type == 'Водород':
            return HydrogenFuelFactory()
        elif fuel_type == 'Уран':
            return UranusFuelFactory()
        elif fuel_type == 'Антиматерия':
            return AntimatterFuelFactory()


class FuelFactory:
    """
    Конкретный топливный завод
    """
    fuel_factory_router = FuelFactoryRouter()

    def create_fuel(self, fuel_type, count_fuel):
        fuel = FuelFactoryRouter().fuel_type_router(fuel_type, count_fuel).create_fuel(count_fuel)
        print(f'Создано {count_fuel} ед. топлива: {fuel}')
        return fuel


if __name__ == "__main__":
    fuel_1 = FuelFactory().create_fuel('Уран', 400)
