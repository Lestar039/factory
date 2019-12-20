import time


class TransportMove:
    """
    Класс, обрабатывающий команды движения транспорта, деталей и расход топлива
    """

    def __init__(self):
        self.type_engine = None
        self.number_engine = None
        self.type_move = None
        self.number_move = None
        self.fuel_consumption = None
        self.type_fuel = None
        self.type_transport = None
        self.transport_speed = None

    def move(self, movement):
        """
        Принимает команды движения. Выводит сообщения о движении транспорта  раз в секунду
        """
        # разбиваем маршрут на направление и количество едениц
        direction_of_travel = movement.split(' ')[0]
        traffic = movement.split(' ')[1]

        # пройденное расстояние за 1 секунду
        move_per_second = self.transport_speed / 3600
        # счетчик пройденного расстояния
        count_move = 0

        # название движения транспорта в отчете в зависимости от типа
        if self.type_transport == 'Наземное':
            type_name = 'Проехал'
        elif self.type_transport == 'Водное':
            type_name = 'Проплыл'
        else:
            type_name = 'Пролетел'

        if direction_of_travel == 'forward' or direction_of_travel == 'back':
            while count_move <= int(traffic):
                for t in range(int(traffic)):
                    if direction_of_travel == 'forward':
                        print(type_name, 'вперед на', f'{move_per_second:.3f}', 'ед.')
                        count_move += move_per_second
                        time.sleep(1)
                    elif direction_of_travel == 'back':
                        print(type_name, 'назад на', f'{move_per_second:.3f}', 'ед.')
                        count_move += move_per_second
                        time.sleep(1)
        elif direction_of_travel == 'left':
            print('Повернул налево на', traffic, 'градусов')
            time.sleep(1)
        elif direction_of_travel == 'right':
            print('Повернул направо на', traffic, 'градусов')
            time.sleep(1)

    def counter_fuel(self, amount_of_fuel):
        """
        Обрабатывает и выводит ссобщения о расходе топлива раз в секунду
        """
        print('Транспорт заправлен', self.type_fuel, 'на', amount_of_fuel, 'ед.')
        counter = (self.transport_speed / 3600) * self.fuel_consumption
        while amount_of_fuel > 0:
            print('Израсходовано', f'{counter:.2f}', 'ед.', self.type_fuel)
            amount_of_fuel -= counter
            time.sleep(1)

    def movement_parts(self):
        """
        Выводит сообщения о пробеге деталей транспорта раз в секунду
        """
        while True:
            if self.number_move >= 1:
                count_part_move = 1
                for count in range(self.number_move):
                    print(self.type_move, ' №', count_part_move, ': пройдено 1 ед.', sep='')
                    count_part_move += 1

            if self.number_engine >= 1:
                count_part_eng = 1
                for count in range(self.number_engine):
                    print('Двигатель ', self.type_engine, ' №', count_part_eng, ': пройдено 1 ед.', sep='')
                    count_part_eng += 1

            time.sleep(1)


class Factory(TransportMove):
    """
    класс фабрика. Производит детали и собирает транспорт
    """

    def __init__(
            self, type_transport, type_engine, number_engine, type_move,
            number_move, type_fuel, fuel_consumption, transport_speed
    ):
        super().__init__()
        self.type_transport = type_transport
        self.type_engine = type_engine
        self.number_engine = number_engine
        self.type_move = type_move
        self.number_move = number_move
        self.type_fuel = type_fuel
        self.fuel_consumption = fuel_consumption
        self.transport_speed = transport_speed

        # Сборка деталей для танспортного средства
        print('>>> Сборка копмонентов для танспортного средства <<<')
        if self.number_engine >= 1:
            for count in range(self.number_engine):
                print('Сборка:', self.type_engine, 'двигатель')
        if self.number_move >= 1:
            for count in range(self.number_move):
                print('Сборка:', self.type_move)
        print('============================================')
        time.sleep(1)
        print('>>> Сборка танспортного средства <<<')
        print("Тип транспортного средства:", self.type_transport)
        print('Двигатель:', self.type_engine, "в количестве", self.number_engine, "шт.")
        print("Движетель:", self.type_move, "в количестве:", self.number_move, "шт.")
        print('Тип топлива:', self.type_fuel)
        print('Расход топлива:', self.fuel_consumption, 'единиц на 1 ед. расстояния')
        print('Скорость:', self.transport_speed, 'ед/ч')
        print('============================================')


class Driver:
    """
    Класс пилота
    """

    def __init__(self, name):
        self.name = name
        print('Создан пилот', self.name)
        print('============================================')


class Start:
    """
    Магический класс для запуска прогаммы
    """
    def __init__(self, transport, fuel, pilot, traffic):
        self.transport = transport
        self.fuel = fuel
        self.pilot = pilot
        self.traffic = traffic

    def start(self):
        pass


# Создаем транспорт
transport_1 = Factory('Наземное', 'Поршневой', 1, 'Колесо', 4, 'Бензин', 20, 2000)
transport_1.counter_fuel(3)
pilot_1 = Driver('John')
transport_1.move('forward 1')
transport_1.move('back 3')
transport_1.move('left 20')
transport_1.move('right 45')
transport_1.movement_parts()

# transport_2 = Factory('Водное', 'Роторный', 2, 'Винт', 2, 'Дизель', 20, 40)
# transport_2.counter_fuel(50)
# transport_2.movement_parts()
# transport_2.move('forward 5')
# transport_2.move('back 3')
# transport_2.move('left 20')
# transport_2.move('right 45')

# transport_3 = Factory('Воздушное', 'Реактивный', 4, 'Реактивное сопло', 4, 'Антиматерия', 5, 4000)
# transport_3.counter_fuel(50)
# transport_3.movement_parts()
# transport_3.move('forward 5')
# transport_3.move('back 3')
# transport_3.move('left 20')
# transport_3.move('right 45')
