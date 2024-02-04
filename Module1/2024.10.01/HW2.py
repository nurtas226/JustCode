class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Student(Person):
    def __init__(self, name, age, stage):
        super().__init__(name, age)
        self._stage = stage

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    def __add__(self, add_salary):
        if isinstance(add_salary, (int, float)):
            self._salary += add_salary
            return self
        else:
            return TypeError("Salary must be a number!")
        
    def __repr__(self):
        return "Empolyee('{}', {}, {})".format(self._name, self._age, self._salary)
                  
roma = Employee('Ramazan', 23, 100000)

roma = roma + 50000

print(roma)

