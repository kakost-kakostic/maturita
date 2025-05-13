from math import sqrt

def load_input():
    return int(input('Zadejte cislo: '))

"""4) Napište program, který z klávesnice přečte zadané celé číslo. Pokud číslo bude 0, vytvořte tabulku malé násobilky.
 Pokud číslo bude 1, vytvořte tabulku velké násobilky."""

def print_multiples(num: int):
    multiples = [i for i in range(1, 11)]
    multiplicators = [i for i in range(11, 21)] if num == 0 else multiples
    chart = ([list(map(lambda x: x*i, multiples)) for i in multiplicators])
    
    max_column_widths = [max(len(str(item)) for item in col) for col in zip(*chart)]
    for row in chart:
        print("  ".join(f"{str(item):<{max_column_widths[i]}}" for i, item in enumerate(row)))

"""5) Na vstupu z klávesnice jsou zadána 3 reálná čísla - koeficienty a, b, c kvadratické rovnice. Vypočítejte kořeny
této rovnice a na monitor zobrazte jeden ze tří možných výstupů: Rovnice má v R dva kořeny x1=…, x2=… 
Rovnice má v R dvojnásobný kořen x1=x2=… Rovnice nemá v R řešení"""
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("Rovnice nemá v R řešení")
    elif discriminant == 0:
        print(f"Rovnice má v R dvojnásobný kořen x1=x2={-b/2*a}")
    else:
        print(f"Rovnice má v R dva kořeny x1={(-b+sqrt(discriminant))/(2*a)} x2={(-b-sqrt(discriminant))/(2*a)} ")

"""6) Na vstupu z klávesnice je zadáno přirozené číslo n Na monitor zobrazte:
prvních n přirozených čísel,
prvních n přirozených sudých čísel počínaje od 2 
prvních n přirozených lichých čísel počínaje od 1 """
def print_nums(n: int):
    print("", [i+1 for i in range(n)], "\n",[i*2+2 for i in range(n)], "\n", [i*2+1 for i in range(n)])

"""7) Na vstupu z klávesnice je zadána řada celých nenulových čísel ukončených nulou (nula je chápána jako značka 
konce řady).Na monitor zobrazte maximum, minimum, součet a průměr čísel z řady.
"""
def load_many_inputs():
    nums = [load_input()]
    while nums[-1] != 0:
        nums.append(load_input())
    return nums[0:-1]

def analyze_nums(nums: list[int]):
    print(f"Maximum:{max(nums)}, minimum:{min(nums)}, součet: {sum(nums)}, průměr: {sum(nums)/len(nums)}")
#4
#print_multiples(loadInput())
#5
#6
print_nums(5)
analyze_nums(load_many_inputs())