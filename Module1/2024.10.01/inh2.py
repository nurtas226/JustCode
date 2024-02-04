# overriding - переопределение методов

# ?! overloading - перегрузка методов ?!


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def say_hi(self):
        print(f"Привет от {self._name}")

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


class Student(Person):
    def __init__(self, name, age, stage):
        super().__init__(name, age)
        self._stage = stage

    def say_hi(self):
        print(f"Привет от студента {self._name}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    def say_hi(self):
        print(f"Привет от сотрудника {self._name}")


ulan = Student('Ulan', 99, 4)
roma = Employee('Ramazan', 40, 100000)

people = [ulan, roma]

for person in people:
    person.say_hi()