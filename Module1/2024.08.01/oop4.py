# __str__() - вызывается во время вывода(print()), форматирования (format <=> f'') и во время преобразования(str())

class Animal:

    def __init__(self, animal_name, animal_sound):
        self.name = animal_name
        self.sound = animal_sound
        self.leg_count = 4

    def say_something(self):
        print(self.sound)

    def __str__(self):
        res = f"{self.name}: говорит {self.sound}, имеет {self.leg_count} ноги."
        # res = "Это экземпляр класса Animal!"
        return res


cat = Animal(animal_name='cat', animal_sound='meaw!')
dog = Animal(animal_name='dog', animal_sound='gav-gav!')

print(cat)