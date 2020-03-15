import time

class Airplane:
    def __init__(self, make, modele, year, max_speed, odometer):
        self.make = make
        self.modele = modele
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        
    def Airplane_info(self):
        print("Информация про наш самолет")
        print(f"Марка {self.make}")
        print(f"Модель {self.modele}")
        print(f"Год выпуска {self.year} г.")
        print(f"Максимальный скорость {self.max_speed}км/час")
        print(f"Пробег {self.odometer}км")
    
    def is_flying(self):
        '''\nКуды вы хотите литать?
    1) Казахстан (5000km)
    2) Россия (10000km)
    3) Америка (50000km)
    4) Канада (52000km)
    '''
        info_is_flying = int(input("Введите номер страны: "))

        if info_is_flying == 1:
            print("Время до Казахстана 1 минут. Сидите тихо и ожидайте")
            local_time = float(1.0)
            local_time = local_time * 60
            print(time.sleep(local_time))
            print('Поздавляем вы приехали в Казахстан.')
            print(f'Пробег самолета был {self.odometer} км, Стало {self.odometer + 5000} км ')
        
        elif info_is_flying == 2:
            print("Время до России 1 минут. Сидите тихо и ожидайте")
            local_time = float(1.0)
            local_time = local_time * 60
            print(time.sleep(local_time))
            print('Поздавляем вы приехали в Россию.')
            print(f'Пробег самолета был {self.odometer} км, Стало {self.odometer + 10000} км ')

        elif info_is_flying == 3:
            print("Время до Америки 1 минут. Сидите тихо и ожидайте")
            local_time = float(1.0)
            local_time = local_time * 60
            print(time.sleep(local_time))
            print('Поздавляем вы приехали в Америку.')
            print(f'Пробег самолета был {self.odometer} км, Стало {self.odometer + 50000} км ')
      
        elif info_is_flying == 4:
            print("Время до Канады 1 минут. Сидите тихо и ожидайте")
            local_time = float(1.0)
            local_time = local_time * 60
            print(time.sleep(local_time))
            print('Поздавляем вы приехали в Канаду.')
            print(f'Пробег самолета был {self.odometer} км, Стало {self.odometer + 52000} км ') 
        else:
            print("В списке нету такого номера или страны")


airplane = Airplane('WayupKG', 'A854', '2020', '500', 10000)
airplane.Airplane_info()
print(airplane.is_flying.__doc__)
airplane.is_flying()


