import math
"""8) Na vstupu je zadáno přirozené číslo n. Vypočtěte n!. Použijte funkce VSTUP, FAKTORIAL, VYSTUP."""
def load_input():
    return int(input('Zadejte cislo: '))
def factorial(n: int):
    x = 1
    for i in range(2,n+1):
        x *= i
    return x
def output_factorial():
    print(factorial(load_input()))

"""9) Vytvořte nabídku dezertů tak, že si uživatel vybere ovoce (1-jahody, 2-maliny, 3 -ostružiny) a
dip (1- šlehačka, 2 – jogurt). Z vybraných ingrediencí bude sestaven dezert).
Použijte funkce choose_fruit, add_dip a choose_dessert."""

fruit = ["jahody", "maliny", "ostružiny"]
dip = ["šlehačka", "jogurt"]
def pick_fruit():
    return fruit[int(input(f"{list(enumerate(fruit))} \nVyber číslo ovoce: "))]

def add_dip():
    return dip[int(input(f"{list(enumerate(dip))} \nVyber číslo dipu: "))]

def pick_dessert():
    print(f"Vybrán dezert: {pick_fruit()} s {add_dip()}.")

"""10) Vytvořte program s ukázkami funkcí z knihovem math a random. """
def kombinatorika(n: int, k: int):
    print(f"Pocet permutaci: {math.factorial(n)}, pocet variaci: {math.perm(n, k)}, pocet kombinaci: {math.comb(n, k)}")

kombinatorika(, 3)
pick_dessert()