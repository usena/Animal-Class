class Animal:
    def __init__(self,animalName):
        self.__animalName=animalName
    def get_animalName(self):
        return self.__animalName
    def __str__(self):
        return f'{self.__animalName} is an animal.'
        
class Mammal(Animal):
    def __init__(self,animalName):
        super().__init__(animalName)
    def __str__(self):
        return f'{super().__str__()}\n{super().get_animalName()} is a warm-blooded animal.'

class NonMarineMammal(Mammal):
    def __init__(self, animalName):
        super().__init__(animalName)
    def __str__(self):
        return f"{super().__str__()}\n{super().get_animalName()} can't swim."

class NonWingedMammal(Mammal):
    def __init__(self, animalName):
        super().__init__(animalName)
    def __str__(self):
        return f"{super().__str__()}\n{super().get_animalName()} can't fly."

class Dog(NonMarineMammal,NonWingedMammal):
    def __init__(self, animalName):
        super().__init__(animalName)
    def __str__(self):
        return f'{super().__str__()}\n{super().get_animalName()} has 4 legs.'

class Bat(NonMarineMammal):
    def __init__(self, animalName):
        super().__init__(animalName)
    def __str__(self):
        return f'{super().__str__()}'

dog = Dog("Dog")
print(dog.__str__())
bat = Bat("Bat")
print(bat.__str__())

