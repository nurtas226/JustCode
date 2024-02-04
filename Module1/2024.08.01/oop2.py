# методы - функции внутри класса


class Animal:

    def say_something(self):
        print("meaw!")


cat = Animal()
dog = Animal()

cat.say_something()
print('--------------------------------')
dog.say_something()