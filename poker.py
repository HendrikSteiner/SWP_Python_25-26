#datestruktur 52 elemente
#lottometohe 5 karten ziehen
#neue liste /13 dividieren -> Farbe
#2 symbole vergleichen -> modulo (gleicher Rest gleiche Farbe)
#sort()
#flush -> set len() --> wenn 1 dann Flush
#seltensten als erstes, wahrscheinlichsten als letztes
import random
from collections import Counter

deck = list(range(52))

def pull_5_cards():
    pulled_cards = random.sample(deck, 5)
    pulled_cards.sort()
    return pulled_cards

def color_card(card):
    return card // 13

def symbol_card(card):
    return card % 13

def flush(cards):
    farben = [color_card(card) for card in cards]
    return len(set(farben)) == 1

def symbols(cards):
    return [symbol_card(card) for card in cards]

def count_symbols(cards):
    return Counter(symbols(cards))

def has_pair(cards):
    counts = count_symbols(cards) #counts = {symbol: count}
    return list(counts.values()).count(2) == 1

def has_two_pair(cards):
    counts = count_symbols(cards)
    return list(counts.values()).count(2) == 2

def has_three_of_a_kind(cards):
    counts = count_symbols(cards)
    return 3 in counts.values()

def has_four_of_a_kind(cards):
    counts = count_symbols(cards)
    return 4 in counts.values()

def has_full_house(cards):
    counts = count_symbols(cards) #dict zählt wie oft Zahl vorkommt
    vals = list(counts.values()) #speichert values als list
    return (3 in vals) and (2 in vals)

def has_straight(cards):
    sortedcards = sorted(symbols(cards))

    if sortedcards == [0, 1, 2, 3, 4]:
        return True

    if sortedcards == [9, 10, 11, 12, 0]:
        return True

    for i in range(1, len(sortedcards)):
        if sortedcards[i] != sortedcards[i-1] + 1:
            return False

    return True

def is_royal_flush(cards):
    if not flush(cards):
        return False
    symbs = sorted(symbols(cards))
    royal = [0, 9, 10, 11, 12]
    return symbs == royal


def combination(cards):
    if is_royal_flush(cards):
        return "Royal Flush"
    elif flush(cards) and has_straight(cards):
        return "Straight Flush"
    elif has_four_of_a_kind(cards):
        return "Vierling"
    elif has_full_house(cards):
        return "Full House"
    elif flush(cards):
        return "Flush"
    elif has_straight(cards):
        return "Straße"
    elif has_three_of_a_kind(cards):
        return "Drilling"
    elif has_two_pair(cards):
        return "Two Pair"
    elif has_pair(cards):
        return "Pair"
    else:
        return "High Card"

def simulate_poker(n):
    result = []
    for _ in range(n):
        cards = pull_5_cards()
        typ = combination(cards)
        result.append(typ)

    unique = set(result)  # Ein Set mit nur einzigartigen Kombinationen

    print("Pokerstatistik (in Prozent):")
    for combi in unique:
        anz = result.count(combi)
        prozent = anz / n * 100
        print(f"{combi}: {prozent:.4f}%")


cards = pull_5_cards()
print("Gezogene Karten:", cards)
print("Kartenfarben:", [color_card(card) for card in cards])
print("Kartensymbole:", [symbol_card(card) for card in cards])
print("Kombination:", combination(cards))

# Simulation starten
simulate_poker(100000)