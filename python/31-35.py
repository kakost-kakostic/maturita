
"""31) Zjistěte, zda 2 řetězce zadané z klávesnice jsou / nejsou anagram (obsahují stejná písmena)"""
def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())
"""32) Zjistěte, zda řetězec zadaný z klávesnice je / není palindrom (čte se stejně zepředu jako zezadu)"""
def is_palindrome(word: str):
    word = word.replace(" ", "")
    return word == word[::-1]
"""33) Zjistěte četnost výskytu písmene a (malého i velkého) v zadaném textovém řetězci"""
def a_count(word: str):
    return len(list(filter(lambda x: x == "a", word.lower())))

"""34) Ze zadaného textového řetězce vytvořte nový textový řetězec, ve kterém se každý znak bude opakovat n krát
(n je zadáno z klávesnice)"""
def multiply_string(string, n):
    return string * n

"""35) Na vstupu z klávesnice je zadaný textový řetězec a přirozené číslo. Zašifrujte řetězec 
Cézarovou šifrou a výsledný řetězec zobrazte na monitor."""
def caesar_cypher(text: str, n:int):
    result = ""
    for character in text:
        if ord(character.lower()) + n <= ord("z"):
            result = result + chr(ord(character) + n)
        else:
            result = result + chr(ord(character) + n - 26)
    return result

print(is_anagram("ahoj", "hojA"))
print(is_palindrome("kobyla ma maly bok"))
print(a_count("ahoj svete aaa aaaAAAA"))
print(multiply_string("ha", 3))
print(caesar_cypher("abcdefghijklmnopqrstuvwxyz", 3))