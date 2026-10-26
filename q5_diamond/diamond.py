"""Q5(b): diamond inheritance in Python."""
NAME = "Tendai"  # TODO: replace with your own name


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super().__init__(name)

    def role(self):
        return "Student"


class Staff(Person):
    def __init__(self, name):
        super().__init__(name)

    def role(self):
        return "Staff"


class TeachingAssistant(Student, Staff):
    def __init__(self, name):
        super().__init__(name)  # MRO ensures Person.__init__ runs once

    def role(self):
        return f"{Student.role(self)} and {Staff.role(self)}"


ta = TeachingAssistant(NAME)
print("Name:", ta.name)
print("Role:", ta.role())
print("MRO :", [c.__name__ for c in TeachingAssistant.__mro__])
