from math import sqrt
"""38) Napište program, který vypočítá celočíselný podíl a zbytek dvou celých čísel. Použijte funkci podíl_a_zbytek,
která bude mít na vstupu 2 celá čísla a na výstup vydá n-tici se dvěma prvky (podíl, zbytek)."""
def podil_a_zbytek(delenec, delitel):
    return delenec // delitel, delenec % delitel

"""39) Na vstupu z klávesnice budou zadána 4 reálná čísla a, b, c, d. Vytvořte z nich 2 komplexní čísla (a,b), (c,d) 
jako dvě dvouprkové n-tice. Vypočítejte součet těchto dvou komplexních čísel. Použijte funkci, na jejímž vstupu budou 
vytvořené n-tice (a,b), (c,d) a na výstupu bude jedna n-tice (e,f), která bude reprezentovat součet vstupních komplexních 
čísel. Výsledné komplexní číslo zobrazte na monitor."""
def input_tuple(n = 2):
    return tuple(int(input("Zadejte cislo: ")) for i in range(n))

def add_complex(a: tuple[int], b: tuple[int]):
    return a[0]+b[0], a[1]+b[1]

"""40) Na vstupu z klávesnice budou zadána 4 reálná čísla x1, y1, x2, y2, která reprezentují souřadnice 2 bodů v rovině.
Vytvořte z nich dvě dvouprkové n-tice (x1,y1), (x2,y2). Vypočítejte vzdálenost těchto dvou bodů. Použijte funkci, na 
jejímž vstupu budou vytvořené n-tice (x1,y1), (x2,y2) a na výstupu bude jedno reálné číslo reprezentující vzdálenost 
vstupních bodů. Výslednou vzdálenost zobrazte na monitor."""

def line_length(a: tuple[int], b: tuple[int]):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

"""41) Ve 3 n-ticích evidujte údaje o 3 zaměstnancích (jméno, příjmení, plat). Vytvořte seznam těchto n-tic, projděte 
jej a najděte pracovníka s nejvyšším platem. Na výstup zobrazte jméno, příjmení a plat nalezeného pracovníka."""
def track_employees(a: tuple[str, str, int], b: tuple[str, str, int], c:tuple[str, str, int]):
    employees = [a, b, c]
    print(sorted(employees, key=lambda x: x[2], reverse=True)[0])


# print(podil_a_zbytek(3, 2))
# print(add_complex(input_tuple(), input_tuple()))
# print(line_length(input_tuple(), input_tuple()))
# track_employees(("Pepa", "Repa", 2000), ("Roman", "Chalan", 2600), ("Evzen", "Zeli", 2500))
