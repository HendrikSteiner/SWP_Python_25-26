import sys

zahlen = [1, 1, 2, 3, 4, 4, 4, 6, 7, 8, 9]

def paare_finden(zahlen, ziel):
    paare = set()
    for i in zahlen:
        for j in range(i, len(zahlen)):
            if zahlen[i] + zahlen[j] == ziel:
                paare.add((zahlen[i], zahlen[j]))
    return paare

def print_paare():
    ziel = 10
    paare = paare_finden(zahlen, ziel)
    if len(paare) == 0:
        print("Keine Paare gefunden")
    else:
        print("Paare mit der Summe {ziel}:")
        for p in paare:
            print(p)
        print(f"Anzahl der Paare: {len(paare)}")

def main():
        print_paare()



if __name__ == "__main__":
    main()
