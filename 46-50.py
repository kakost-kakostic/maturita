class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

my_bike = Bike("Moje kolo", "modra")

class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades
    def add_grade(self, grade: int):
        self.grades.append(grade)
    def get_average(self):
        if len(self.grades) == 0:
            return None
        return sum(self.grades)/len(self.grades)

pp = Student("Petr Pavel", [2,5,1,4,4,4,2,3])
print(pp.get_average())

class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def get_info(self):
        return self.name, self.pay

    @staticmethod
    def needs_a_raise():
        return True

class Manager(Employee):
    def __init__(self, name, pay, department):
        super().__init__(name, pay)
        self.department = department

hruskin = Manager("jirkin", 40000, "storefront")
print(hruskin.get_info())
print(hruskin.needs_a_raise())

class Animal:
    def __init__(self, name: str):
        self.name = name
    @staticmethod
    def make_noise():
        raise ValueError("Unspecified animal makes no noise. ")
    def introduce(self):
        return f"Ahoj, ja jsem {self.name} a delam {self.make_noise()}."

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def make_noise():
        return "Haf haf"


lizard = Dog("Lizzy")
print(lizard.introduce())

class StFunc:
    @staticmethod
    def is_friend_shaped():
        return True

