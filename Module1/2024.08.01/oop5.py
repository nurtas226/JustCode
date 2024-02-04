# __str__() - вызывается во время вывода(print()), форматирования (format <=> f'') и во время преобразования(str())

class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def say_something(self):
        print(self.sound)

    def __str__(self):
        res = f"{self.name}: говорит {self.sound}"
        return res


class Bird (Animal):

    def __init__(self, name, sound, wing):
        super().__init__(name, sound)
        self.wing = wing

    # def __str__(self):
    #     res = f"{self.name}: говорит {self.sound}, " \
    #           f"размах крыльев {self.wing} см."
    #     return res


class Test (Animal):

    def __init__(self, name, sound, fangs):
        super().__init__(name, sound)
        self.fangs = fangs

    def __str__(self):
        res = f"{self.name}: говорит {self.sound}, " \
              f"кол-во клыков {self.fangs}."
        return res


eagle = Bird(name='eagle', sound='chick-chirick!', wing=160)
wolf = Test(name='wolf', sound='chick-chirick!', fangs=36)

print(eagle)
# eagle.say_something()