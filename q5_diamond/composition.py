"""Q5(d): composition alternative (has-a instead of is-a)."""
NAME = "Tendai"  # TODO: replace with your own name


class Person:
    def __init__(self, name):
        self.name = name


class StudentRecord:
    def __init__(self, student_no):
        self.student_no = student_no

    def role(self):
        return "Student"


class StaffRecord:
    def __init__(self, staff_no):
        self.staff_no = staff_no

    def role(self):
        return "Staff"


class TeachingAssistant(Person):
    def __init__(self, name, student_no, staff_no):
        super().__init__(name)
        self.student = StudentRecord(student_no)  # has-a
        self.staff = StaffRecord(staff_no)        # has-a

    def role(self):
        return f"{self.student.role()} and {self.staff.role()}"


ta = TeachingAssistant(NAME, "S1001", "T2001")
print("Name:", ta.name)
print("Role:", ta.role())
