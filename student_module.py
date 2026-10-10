# student_module.py
# Module containing classes and functions for the Student Grade System

class Person:
    """PARENT CLASS (for Inheritance requirement d)"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"{self.name} ({self.age} years old)"


class Student(Person):
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = marks

    def calculate_average(self):
        if not self.marks:
            raise ValueError("No marks provided.")
        return sum(self.marks) / len(self.marks)

    def generate_grade(self):
        avg = self.calculate_average()
        if avg >= 80:   return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        elif avg >= 50: return "D"
        else:           return "F"

    def display_info(self):
        return (f"[Student] {self.name} | ID: {self.student_id} "
                f"| Avg: {self.calculate_average():.2f} | Grade: {self.generate_grade()}")


class HonourStudent(Student):
    def __init__(self, name, age, student_id, marks, bonus=5):
        super().__init__(name, age, student_id, marks)
        self.bonus = bonus

    def calculate_average(self):
        base = super().calculate_average()
        return min(base + self.bonus, 100)

    def display_info(self):
        return (f"[Honour Student] {self.name} | ID: {self.student_id} "
                f"| Avg(+bonus): {self.calculate_average():.2f} "
                f"| Grade: {self.generate_grade()}")


def calculate_total_marks(marks):
    return sum(marks)


def determine_status(average, passing_mark=50):
    if average >= passing_mark:
        return "PASS"
    return "FAIL"


