##"Множественное наследование"#module_6_3
##Задача "Ошибка эволюции":
import random


class Animal:
    def __init__(self, live=True, sound=None, _DEGREE_OF_DANGER=0):
        _cords = [0, 0, 0]
        speed = 1

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            _cords[0] += speed * dx
            _cords[1] += speed * dy
            _cords[1] += speed * dz
        return (cords)

    def get_cords(self):
        print(f'X: {_cords[0]} Y: {_cords[1]} Z: {_cords[2]}')

    def attack(self):
        if _DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self)


class Bird(Animal):
    def __init__(self):
        super().__init__(self)

    beak = True

    def lay_eggs(self):
        print("Here are(is) {random[1, 2, 3, 4]} eggs for you")


class AquaticAnimal(Animal ):
    def __init__(self, _DEGREE_OF_DANGER = 3):
        super().__init__(self)


    def dive_in(self, dz):
        _cords[2] -= speed / 2 * abs(dz)
        return (_cords)


class PoisonousAnimal(Animal):
    def __init__(self, _DEGREE_OF_DANGER=8):
        def __init__(self):
            super().__init__(self)

    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, _DEGREE_OF_DANGER=8):
        def __init__(self):
    sound = "Click-click-click"


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
