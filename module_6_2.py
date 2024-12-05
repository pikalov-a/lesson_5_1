##"Доступ к свойствам родителя. Переопределение свойств"#module_6_2
##Задача "Изменять нельзя получать":
class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        #        self.__COLOR_VARIANTS = __COLOR_VARIANTS
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        def get_model(__model):
            return(f'Модель: {self.__model}')

        def get_horsepower(__engine_power):
            return(f'Мощность двигателя: {self.__engine_power}')

        def get_color(__color):
            return(f'Цвет: {self.__color}')

        def print_info():
            print(get_model(self.__model))
            print(get_horsepower(self.__engine_power))
            print(get_color(self.__color))
            print(f'Владелец: {self.owner}')

        def set_color(__color, new_color):
            if new_color.lower in __COLOR_VARIANTS:
                __color = new_color
            else:
                print(f'Нельзя сменить цвет на {new_color}')

        __COLOR_VARIANTS = ['white', 'yellow', 'brown', 'orange', 'violet', 'red', 'blue', 'green', 'black', 'other']
#        print_info()


class Sedan(Vehicle):
    def __init__(self, owner, __model, __color, __engine_power):
        super().__init__( owner, __model, __color, __engine_power)
        super().print_info()
    #    super(Vehicle).__init__(Vehicle)
    #    super(Vehicle).print_info(self, owner)
    #        self.__COLOR_VARIANTS = __COLOR_VARIANTS)

    __PASSENGERS_LIMIT = 5


# __COLOR_VARIANTS = ['white', 'yellow', 'brown', 'orange', 'violet', 'red', 'blue', 'green', 'black', 'other']
#Sedan= Sedan ('Fedos', 'Toyota Mark II', 'blue', 500 )
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
#Vehicle.print_info('Fedos', 'Toyota Mark II', 'blue', 500)
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
