class Animal:
    def __init__(self, animal_name):
        self.name = animal_name

    def get_name(self):
        return self.name

class AnimalDB:
    def get(self, id) -> Animal:
        pass

    def save(self, id, animal_name) -> Animal:
        pass