# =====> Топливо <=====
class AbstractFuel:
    _name = 'abstract_fuel'

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
    count_fuel = 0

    def create_fuel(self):
        raise NotImplementedError


class PetrolFuelFactory(AbstractFuelFactory):
    """
    Завод по производству бензина
    """

    def create_fuel(self):
        return PetrolFuel()


class DieselFuelFactory(AbstractFuelFactory):
    """
     Завод по производству дизеля
    """

    def create_fuel(self):
        return DieselFuel()


class BatteryFuelFactory(AbstractFuelFactory):
    """
    Завод по производству аккумуляторов
    """

    def create_fuel(self):
        return BatteryFuel()


class HydrogenFuelFactory(AbstractFuelFactory):
    """
    Завод по производству водорода
    """

    def create_fuel(self):
        return HydrogenFuel()


class UranusFuelFactory(AbstractFuelFactory):
    """
    Завод по производству урана
    """

    def create_fuel(self):
        return UraniumFuel()


class AntimatterFuelFactory(AbstractFuelFactory):
    """
    Завод по производству антиматерии
    """

    def create_fuel(self):
        return AntimatterFuel()


class FuelFactory:

    def create_fuel(self, fuel):
        if fuel == 'Бензин':
            return PetrolFuelFactory().create_fuel()
        elif fuel == 'Дизель':
            return DieselFuelFactory().create_fuel()
        elif fuel == 'Электричество':
            return BatteryFuelFactory().create_fuel()
        elif fuel == 'Водород':
            return HydrogenFuelFactory().create_fuel()
        elif fuel == 'Уран':
            return UranusFuelFactory().create_fuel()
        elif fuel == 'Антиматерия':
            return AntimatterFuelFactory().create_fuel()


# =====> test <=====
fuel_1 = FuelFactory().create_fuel('Уран')
print(fuel_1.count_fuel)
