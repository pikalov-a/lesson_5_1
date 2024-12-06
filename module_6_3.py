##"Множественное наследование"#module_6_3
##Задача "Ошибка эволюции":
import random


class Animal:
    def __init__(self, live=True, sound=None, _DEGREE_OF_DANGER=0):
#        cords = [0, 0, 0]
#        speed = 1
        self._cords = [0, 0, 0]
#        print(self._cords)
#        self.speed = 10
        self.live=True
        self.sound=sound
#        self._DEGREE_OF_DANGER=0


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
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self)


class Bird(Animal):
    def __init__(self, **kvargs):
        super().__init__(**kvargs)

    beak = True

    # def lay_eggs(self):
    #     print(f"Here are(is) {random.choice[1, 2, 3, 4]} eggs for you")

    def lay_eggs(self):
        print(f"Here are {random.choice([1, 2, 3, 4])} eggs for you")


class AquaticAnimal(Animal ):
    def __init__(self, **kvargs):
        super().__init__(**kvargs)

#    def __init__(self, _DEGREE_OF_DANGER = 3):
#        super().__init__(self)


    def dive_in(self, dz):
        self._cords[2] -= self.speed / 2 * abs(dz)
        return self._cords


class PoisonousAnimal(Animal):
    def __init__(self, **kvargs):
        super().__init__(**kvargs)

#    def __init__(self, _DEGREE_OF_DANGER=8):
#        super().__init__(self)

    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
#    def __init__(self, **kvargs):
#        super().__init__(**kvargs)

    def __init__(self, speed):
        self.live = True
        self.speed = 10
        self.sound = "Click-click-click"
        print("!!!!",self.sound)
        super().__init__() ##если отключить, sound работает, а move не работает
        print("11111",self.sound)
        self.sound = "Click-click-click"  # все равно не крякает!!!!
        print("00000",self.sound)
#        self.move()




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
