# Задача "Ошибка эволюции"
import random
class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if (self._cords[2] + dz * self.speed) < 0:
            print( "It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        print("DEGREE_OF_DANGER", self._DEGREE_OF_DANGER)
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        print(self.sound if self.sound else "No sound")

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")

class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed / 2

class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
        self.sound = "Click-click-click"

db = Duckbill(10)
print(db.live) 
print(db.beak) # Проверяем звук
db.speak()  # Утконос говорит
db.attack()  # Проверяем, атакует ли он
db.move(1, 2, 3)  # Изменяем координаты
db.get_cords()  # Печатаем текущие координаты
db.dive_in(6)  # Утконос ныряет
db.get_cords()  # Печатаем координаты после ныряния
db.lay_eggs()  # Утконос откладывает яйца