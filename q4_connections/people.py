"""Q4(c): construction and cleanup order."""
NAME = "Tendai"  # TODO: replace with your own name


class Person:
    def __init__(self, name):
        self.name = name
        print("Person built:", name)

    def __del__(self):
        print("Person cleaned up:", self.name)


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        print("Student built:", name)

    def __del__(self):
        print("Student cleaned up:", self.name)
        super().__del__()


class GradStudent(Student):
    def __init__(self, name):
        super().__init__(name)
        print("GradStudent built:", name)

    def __del__(self):
        print("GradStudent cleaned up:", self.name)
        super().__del__()


g = GradStudent(NAME)
del g  # in CPython the object is freed immediately
