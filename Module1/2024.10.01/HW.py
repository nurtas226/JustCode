class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
class Student(Person):
    def __init__(self, name, age, stage):
        super().__init__(name, age)
        self._stage = stage
    
    def __add__(self, other):
        if isinstance(other, Student):
            new_student = Student(self._name, self._age, self._stage + other._stage)
            return new_student
        else:
            return "Error occured"
    def __repr__(self):
        return "Student('{}', {}, {})".format(self._name, self._age, self._stage)

student1 = Student('Max', 23, 2)
student2 = Student('Vadim', 24, 1)

result = student1 + student2

print(result)