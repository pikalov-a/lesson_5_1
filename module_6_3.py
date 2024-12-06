##"Множественное наследование"#module_6_3
##Задача "Ошибка эволюции":
import random

class Animal:
    def __init__(self, live=True, sound=None, degree_of_danger=0, speed=10): #добавили speed
        self._cords = [0, 0, 0]
        self.live = live
        self.sound = sound
        self.degree_of_danger = degree_of_danger
        self.speed = speed


    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += self.speed * dx
            self._cords[1] += self.speed * dy
            self._cords[2] += self.speed * dz
        return self._cords

    def get_cords(self):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

    def attack(self):
        if self.degree_of_danger < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("...")


class Bird(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.beak = True

    def lay_eggs(self):
        print(f"Here are {random.choice([1, 2, 3, 4])} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, degree_of_danger=3, **kwargs):
        super().__init__(degree_of_danger=degree_of_danger, **kwargs)

    def dive_in(self, dz):
        self._cords[2] -= self.speed / 2 * abs(dz)
        return self._cords


class PoisonousAnimal(Animal):
    def __init__(self, degree_of_danger=8, **kwargs):
        super().__init__(degree_of_danger=degree_of_danger, **kwargs)


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed=10):
        self.live = True
        self.speed = speed
        self.sound = "Click-click-click"
        super().__init__(speed=self.speed)
        super().__init__(sound = "Click-click-click") #спасибо за подсказку, увидел, догадался

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
