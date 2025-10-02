import random

def lottoziehung():
    zahlen = list(range(1, 46))
    n = 45
    gezogene = []

    for _ in range(6):
        zufalls_index = random.randint(0, n - 1)
        gezogene_zahl = zahlen[zufalls_index]
        gezogene.append(gezogene_zahl)

        temp = zahlen[zufalls_index]
        zahlen[zufalls_index] = zahlen[n - 1]
        zahlen[n - 1] = temp

        n = n - 1

    return gezogene

def lotto_statistik(ziehungen=1000):
    statistik = {}

    for zahl in range(1, 46):
        statistik[zahl] = 0

    for _ in range(ziehungen):
        zahlen = lottoziehung()
        for zahl in zahlen:
            statistik[zahl] += 1

    return statistik

print("Gezogene Lottozahlen:", lottoziehung())

stat = lotto_statistik()
print("Zahl    Anzahl der Ziehungen")
for zahl in sorted(stat.keys()):
    print(f"{zahl:2d}      {stat[zahl]}")
