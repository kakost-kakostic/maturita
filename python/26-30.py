
"""26) Na vstupu je dán vzor, který budeme hledat v následující řadě čísel (vzor se v řadě může vyskytnout nejvýše jednou).
 Dále je na vstupu dáno přirozené číslo n (označující počet prvků v následující řadě čísel) a vlastní řada n čísel.
 Pomocí metody sekvenčního hledání určete, zda se zadaný vzor v řadě vyskytuje, či nikoliv."""
def linear_search(pattern: int, sequence: list):
    for i in range(len(sequence)):
        if sequence[i] == pattern:
            return i
    return None

"""27) Na vstupu je dán vzor, který budeme hledat v následující řadě čísel (vzor se v řadě může vyskytnout nejvýše jednou).
 Dále je na vstupu dáno přirozené číslo n (označující počet prvků v následující řadě čísel) a vlastní řada n čísel.
 Pomocí metody binárního hledání (= metodou půlení intervalu) určete, zda se zadaný vzor v řadě vyskytuje, či nikoliv."""
def binary_search(pattern: int, sequence: list):
    sss = sorted(sequence)
    low = 0
    high = len(sss) - 1
    while low <= high:
        mid = (high + low) // 2
        if sss[mid] < pattern:
            low = mid + 1
        elif sss[mid] > pattern:
            high = mid - 1
        else:
            return sequence.index(sss[mid])
    return None


"""28) Zadanou řadu čísel seřaďte vzestupně metodou Select Sort"""
def selection_sort(array: list):
    for i in range(len(array) - 1):
        low = i
        for j in range(i+1, len(array)):
            low = j if array[j] < array[low] else low
        array[i], array[low] = array[low], array[i]
    return array

"""29) Zadanou řadu čísel seřaďte vzestupně metodou Insert Sort"""
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
"""30) Zadanou řadu čísel seřaďte vzestupně metodou Quick Sort"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

sequence1 = [27, 85, 3, 68, 49, 33, 7, 73, 42, 59, 96, 20, 16, 70, 91, 11, 24, 38, 64, 80]
patt1 = 3
print(linear_search(patt1, sequence1))
print(binary_search(patt1, sequence1))
print(selection_sort(sequence1))
print(insertion_sort(sequence1))
print(quick_sort(sequence1))