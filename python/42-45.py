"""42) Na vstupu z klávesnice je zadaný text. Na výstup zobrazte reprezentaci tohoto textu Morseovou abecedou.
K převodu využijte slovník."""
translation = dict([('a', '.-'), ('b', '-...'), ('c', '-.-.'), ('d', '-..'), ('e', '.'), ('f', '..-.'),
                         ('g', '--.'), ('h', '....'), ('i', '..'), ('j', '.---'), ('k', '-.-'), ('l', '.-..'),
                         ('m', '--'), ('n', '-.'), ('o', '---'), ('p', '.--.'), ('q', '--.-'), ('r', '.-.'),
                         ('s', '...'), ('t', '-'), ('u', '..-'), ('v', '...-'), ('w', '.--'), ('x', '-..-'),
                         ('y', '-.--'), ('z', '--..'), (' ', '')])
def transcribe_to_morse(text):
    return "/".join(translation.get(i) for i in text.lower())

"""43) Na vstupu z klávesnice je zadán text. Slovníkem reprezentujte počet výskytů jednotlivých písmen v 
zadaném textu a vytvořený slovník zobrazte na monitor."""
def frequency_analysis(text):
    frequency = {}
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

"""44) Na vstupu je zadaný slovník, který obsahuje názvy dezertů (hodnoty) a ceny dezertů (klíče). 
Vytvořte nový slovník, který bude obsahovat tytéž položky jako původní slovník a 
ty budou setříděné podle abecedy podle názvů dezertů."""
desserts={    "Ice cream":10,    "Brownies":12,    "Cheesecake":3,    "Swiss roll":3,    "Cookies":4,    "Cup cake":2 }
def sort_menu(menu):
    return dict(sorted(menu.items()))

"""45) Na vstupu je zadaný slovník, který obsahuje názvy dezertů (hodnoty) a ceny dezertů (klíče). Vytvořte nový slovník,
který bude obsahovat tytéž položky jako původní slovník a ty budou setříděné vzestupně podle ceny (sestupně podle ceny)."""
def reverse_menu(menu):
    return dict(sorted(dict([(b, a) for (a, b) in menu.items()]).items()))

print(transcribe_to_morse("ab ba lulw"))
print(frequency_analysis("haha"))
print(sort_menu(desserts))
print(reverse_menu(desserts))