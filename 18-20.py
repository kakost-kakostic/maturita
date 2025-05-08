from random import sample
"""18) Na vstupu je zadáno přirozené číslo n. Stanovte všechny jeho přirozené dělitele."""
def count_dividers(n: int):
    print(list(filter(lambda x: n % x == 0,[i for i in range(2,n+1)])))

"""19) Na vstupu je zadána řada číselných hodnot, ve které se mohou čísla opakovat. Na výstup zobrazte tutéž řadu čísel,
 každé číslo se v ní však bude vyskytovat pouze jednou (tedy vstupní řada bez duplikátů)."""
def remove_duplicates(nums: list[int]):
    print(list(set(nums)))

"""20) Vygenerujte seznam 6 různých náhodných přirozených. čísel z intervalu 1 až 49
(např. čísla, která uživatel vsadil ve Sportce). Dále vygenerujte další seznam 6 různých náhodných přirozených
čísel z intervalu 1 až 49 (např. čísla, která byla skutečně tažena). Určete, kolik čísel je shodných v obou seznamech."""
def gamble():
    bets = sample(range(1, 49), 6) # funkce sample je použita kvůli duplicitním hodnotám
    pulls = sample(range(1, 49), 6)
    result = [i for i in bets if i in pulls]
    print(f"Uspesne vsazeno {len(result)} čísel: {result}")

count_dividers(6)
remove_duplicates([1, 2, 3, 1, 4, 0])
gamble()

