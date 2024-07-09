class Vehicle:
    __COLOR_VARIANT = ['blue', 'black', 'white', 'red', 'green']

    def __init__(self,owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = int(engine_power)
        self.__color = color

    def get_model(self):
        return f'модель: {self.__model}'

    def get_horsepower(self):
        return f'мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(),
              self.get_horsepower(),
              self.get_color())

    def set_color(self,new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANT]:
            self.__color = new_color
        else:
            print(f'нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vecicle1 = Sedan('Fedos','Toyota Mark ||',500, 'blue')
vecicle1.print_info()

vecicle1.set_color('Pink')
vecicle1.set_color('BLACK')
vecicle1.owner = 'Vasyok'
vecicle1.print_info()
