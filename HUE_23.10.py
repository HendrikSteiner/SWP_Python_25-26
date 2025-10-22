# 1. Set-Funktionalität simulieren
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))] #not für Verneinung if not in seen -> true

liste = [1, 2, 3, 1, 2, 4, 5]
ergebnis = remove_duplicates(liste)
print(ergebnis)

# 2. Dictionary Comprehension mit englischen Buchstaben als Schlüssel
import string
englische_chars = string.ascii_lowercase

result_dict = {char: i+1 for i, char in enumerate(englische_chars)} #char key i++ value
#enumerate erzeugt eine Liste von Tupeln (index, char)
# , trennt tuple in Index und char

print(result_dict)

