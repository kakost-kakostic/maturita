from random import randrange

def print_matrix(matrix):
    for row in matrix:
        print(", ".join(str(x) for x in row))

def matrix_from_input(width = 3, length = 3):
    return [[int(input('Zadejte cislo: ')) for j in range(width)] for i in range(length)]

"""21) Naplňte 2D seznam (matici) o rozměru 3*3 celými čísly a zobrazte ji na monitor."""

def generate_matrix(width = 3, length = 3):
    matrix = [[randrange(0, 49) for j in range(width)] for i in range(length)]
    print_matrix(matrix)

"""22) Na vstupu je zadáno přirozené číslo (max 30), které označuje velikost čtvercové matice. Vytvořte matici, jejíž 
prvky budou mít v hlavní a vedlejší diagonále hodnotu 1, jinak 0. Výslednou matici zobrazte na monitor."""
def generate_zero_matrix(size = 3):
    matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    print_matrix(matrix)


"""23) Naplňte matici 3*3 celými čísly zadanými z klávesnice. Na monitor zobrazte součet všech prvků matice, maximální 
a minimální prvek matice."""

def count_matrix_stats():
    matrix = matrix_from_input()
    min_val = min(min(row) for row in matrix)
    max_val = max(max(row) for row in matrix)
    sum_val = sum(sum(i) for i in matrix)
    print(f"Minimum:{min_val}, maximum:{max_val}, součet:{sum_val}")
    return matrix

"""24) Naplňte matici 3*3 celými čísly zadanými z klávesnice. Vytvořte tříprvkový seznam, který bude obsahovat součty 
jednotlivých řádků a další tříprvkový seznam, který bude obsahovat součty jednotlivých sloupců. Na monitor zobrazte 
původní matici a oba seznamy se součty."""
def count_rows_and_cols():
    matrix = matrix_from_input()
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
    print_matrix(matrix)
    print(row_sums)
    print(col_sums)


"""25) Naplňte matici 3*3 celými čísly. Vytvořte transponovanou matici.
Původní i transponovanou matici zobrazte na monitor.]]"""
def transpose_matrix():
    matrix = matrix_from_input()
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))]for i in range(len(matrix[0]))]
    print_matrix(matrix)
    print_matrix(transposed_matrix)

#
# generate_matrix()
# generate_zero_matrix(6)
# count_matrix_stats()
# count_rows_and_cols()
transpose_matrix()