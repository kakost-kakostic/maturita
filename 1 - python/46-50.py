from abc import ABC, abstractmethod
"""46) Nadefinujte třídu Auto, která bude obsahovat 4 metody: - kosnstruktor, který bude inicializovat atributy jmeno
(majitele), barvu a rychlost - metodu majitel, která na monitor zobrazí jméno majitele auta - metodu barevnost, která
na monitor zobrazí barvu auta - metodu vykon, která na monitor zobrazí maximální rychlost auta Vytvořte dvě instance
třídy Auto (tedy 2 objekty), nazvěte je auto_1 a auto_2 a aplikujte na ně metody majitel, barevnost a vykon
(př. 46a, 46b) Na jednoduchém příkladu vysvětlete pojem viditelnost proměnných (př. 46c)"""

class Bike:
    def __init__(self, name, color, speed):
        self._name = name
        self._color = color
        self._speed = speed
        self.__secret = None
    def print_name(self):
        print(self._name)

    def print_color(self):
        print(self._color)

    def print_speed(self):
        print(self._speed)

bike1 = Bike("Dan", "zelena",100)
bike2 = Bike("Adam", "modra", 80)
bike2.print_name()
print(bike2._name)
print(bike1._Bike__secret) #tomuhle se říká name mangling


"""47) Nadefinujte třídu Student, která bude obsahovat 3 metody: - kosnstruktor, který bude inicializovat atributy jméno
studenta a seznam jeho známek - metodu pridat_znamku, která ke stávajícímu seznamu přidá zadanou známku - metodu 
prumerna_znamka, která vypočítá průměr ze známek uložených v seznamu a zobrazí jej na monirtor Vytvořte instanci třídy 
student (tedy objekt), nazvěte jeje student_1, metodou pridat_znamku postupně přidejte 4 známky do jeho seznamu známek. 
Metodou prumerna_znamka vypočítejte průměr známek zobrazte jej na monitor."""
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
pp.add_grade(5)
print(pp.get_average())
"""48) Nadefinujte třídu Zamestnanec, která bude obsahovat 2 metody: - kosnstruktor, který bude inicializovat atributy 
jméno zaměstnance a jeho plat - metodu zobraz_informace, která jméno a plat zaměstnance zobrazí na monitor. Dále 
nadefinujte třídu Manazer, která bude odvozená ze třídy zaměstnanec (zdědí její metody i atributy) a navíc bude u 
manažera evidovat název oddělení, které vede. Vytvořte instanci třídy Zamestnanec, nazvěte ji zamestnanec_1 a metodou 
zobraz_informace zobrazte na monitor jeho jméno a plat. Vytvořte instanci třídy Manazer, nazvěte ji manazer_1 a metodou 
zobraz_informace zobrazte na monitor jeho jméno, plat a název oddělení, které vede.
"""
class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def get_info(self):
        print(self.name, self.pay)

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
"""49) Nadefinujte třídu Zviratko, která bude obsahovat 3 metody: - kosnstruktor, který bude inicializovat atribut jméno
zvířete - metodu jmenuji_se, která zobrazí jméno zvířete na monitor - metodu zvuk, která bude defována až v podtřídách. 
Dále nadefinujte podtřídy Pes, Kocka, Krava třídy Zvire, které budou obsahovat vlastní implementaci metody zvuk. 
Použijte výjimku NotImplementedError."""
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_noise(self):
        raise ValueError("This method is not implemented in the base class.")
    def introduce(self):
        return f"Ahoj, ja jsem {self.name} a delam {self.make_noise()}."

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        return "Haf haf"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        return "Mňau"

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)


    def make_noise(self):
        return "Bů"

lizard = Dog("Lizzy")
print(lizard.introduce())

"""50) Předchozí příklad vyřešte pomocí abstraktních tříd a metod."""

class Animal(ABC):
    def __init__(self, name):
        self.name = name  # Veřejný atribut jméno

    def introduce(self):
        print(f"Ahoj, mé jméno je {self.name}")

    @abstractmethod
    def make_noise(self):
        pass

class Dog(Animal):
    def make_noise(self):
        return "Haf haf"