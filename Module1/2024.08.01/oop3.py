# методы - функции внутри класса
# поля - переменные внутри класса   / своиства

# dunder методы - double under / магические методы
# конструктор = def __init__()


class Animal:

    def __init__(self, sound):  # self = dog, sound = 'gav_gav!'
        self.sound = sound
        self.leg_count = 4

    def say_something(self):
        print(self.sound)


cat = Animal(sound='meaw!')
dog = Animal(sound='gav-gav!')

dog.is_pet = True
cat.say_something()
dog.say_something()


print("main:", dog.sound)
print("main:", dog.leg_count)
print("main:", dog.is_pet)