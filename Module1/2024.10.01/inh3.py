#  a = a + b
#  a += b


class Person(object):
    def __init__(self, name, surname, gender):
        self._name = name
        self._surname = surname
        self._gender = gender

    def say_hi(self):
        print(f"Привет от {self._name}")

    def __str__(self):
        return f"{self._name} {self._surname}"

    def __add__(self, other):
        new_person = Person('Roma', self._surname + '-' + other._surname, 'male')
        return new_person
        # return f"Ты пытаешься прибавить {self} к {other}"


alisa = Person('Alisa', 'Petrova', 'female')
maxim = Person('Max', 'Orlov', 'male')

print(alisa)

result = maxim + alisa
print(type(result))
print(result)



# maxim += alisa
# print(type(maxim))
# print(maxim)