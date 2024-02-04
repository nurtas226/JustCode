# геттер - getter   -  возвращает поле
# сеттер - setter -  меняет поле

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age


ulan = Person('Ulan', 99)
roma = Person('Roma', 100)

print("Перед изменением: ", ulan.get_name())

ulan.set_name('Max')

print("После изменения: ", ulan.get_name())