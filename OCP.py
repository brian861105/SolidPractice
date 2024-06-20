class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass
    
    def make_sound(self) -> str:
        pass


class Lion(Animal):
    def make_sound(self) -> str:
        return 'roar'


class Cat(Animal):
    def make_sound(self) -> str:
        return 'Mow'


class Dog(Animal):
    def make_sound(self) -> str:
        return "woof"


animals = [Lion("Lion"), Cat("Cat"), Dog("Dog")]


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animal_sound(animals)