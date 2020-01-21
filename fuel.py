# =====> Топливо <=====
class AbstractFuel:
    _name = 'абстрактное топливо'

    def burn(self):
        raise NotImplementedError

    def __str__(self):
        return self._name


class PetrolFuel(AbstractFuel):
    _name = 'Бензин'

    def burn(self):
        return 'Расходуется бензин'


class DieselFuel(AbstractFuel):
    _name = 'Дизель'

    def burn(self):
        return 'Расходуется дизель'


class BatteryFuel(AbstractFuel):
    _name = 'Батарея'

    def burn(self):
        return 'Расходуется батарея'


class HydrogenFuel(AbstractFuel):
    _name = 'Водород'

    def burn(self):
        return 'Расходуется водород'


class UraniumFuel(AbstractFuel):
    _name = 'Уран'

    def burn(self):
        return 'Расходуется уран'


class AntimatterFuel(AbstractFuel):
    _name = 'Антиматерия'

    def burn(self):
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
        return PetrolFuel()


class DieselFuelFactory(AbstractFuelFactory):
    """
     Завод по производству дизеля
    """

    def create_fuel(self, count_fuel):
        return DieselFuel()


class BatteryFuelFactory(AbstractFuelFactory):
    """
    Завод по производству аккумуляторов
    """

    def create_fuel(self, count_fuel):
        return BatteryFuel()


class HydrogenFuelFactory(AbstractFuelFactory):
    """
    Завод по производству водорода
    """

    def create_fuel(self, count_fuel):
        return HydrogenFuel()


class UranusFuelFactory(AbstractFuelFactory):
    """
    Завод по производству урана
    """

    def create_fuel(self, count_fuel):
        return UraniumFuel()


class AntimatterFuelFactory(AbstractFuelFactory):
    """
    Завод по производству антиматерии
    """

    def create_fuel(self, count_fuel):
        return AntimatterFuel()


class FuelFactory:
    """
    Конкретный топливный завод
    """

    def create_fuel(self, fuel, count_fuel):
        if fuel == 'Бензин':
            print(f'Создано {count_fuel} ед. топлива: {fuel}')
            return PetrolFuelFactory().create_fuel(count_fuel)
        elif fuel == 'Дизель':
            print(f'Создано {count_fuel} ед. топлива: {fuel}')
            return DieselFuelFactory().create_fuel(count_fuel)
        elif fuel == 'Электричество':
            print(f'Создано {count_fuel} ед. топлива: {fuel}')
            return BatteryFuelFactory().create_fuel(count_fuel)
        elif fuel == 'Водород':
            print(f'Создано {count_fuel} ед. топлива: {fuel}')
            return HydrogenFuelFactory().create_fuel(count_fuel)
        elif fuel == 'Уран':
            print(f'Создано {count_fuel} ед. топлива: {fuel}')
            return UranusFuelFactory().create_fuel(count_fuel)
        elif fuel == 'Антиматерия':
            print(f'Создано {count_fuel} ед. топлива: {fuel}')
            return AntimatterFuelFactory().create_fuel(count_fuel)


if __name__ == "__main__":
    fuel_1 = FuelFactory().create_fuel('Уран', 400)
