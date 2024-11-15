class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
       self.owner = owner
       self._model = model
       self._color = color
       self._engine_power = engine_power

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(f'Модель: {self._model}')
        print(f'Мощность двигателя: {self._engine_power}')
        print(f'Цвет: {self._color}')
        print(f'Владелец: {self.owner}')

    def set_color(self,  new_color: str):
        if new_color in self.__COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('black')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
