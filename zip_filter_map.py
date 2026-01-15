#
#names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
#ages = [23, 17, 34, 15, 29]
#scores = [88, 92, 75, 64, 91]

#Erzeuge aus diesen Listen eine gefilterte Liste von Personen, die folgende Bedingungen erfüllt:

#Alter ≥ 18 und Score ≥ 80

#müssen verwendet werden:

#zip – kombiniere die drei Listen so, dass jeder Eintrag ein Tupel (name, age, score) ist.

#filter + lambda – filtere alle Personen heraus, die beide Bedingungen erfüllen.

#map + lambda – forme jedes Tupel in ein Dictionary der Form
#{"name": ..., "age": ..., "score": ...} um.

#{"name": "Anna", "age": 23, "score": 88}


names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

personen = zip(names, ages, scores)

gefiltert = filter(lambda p: p[1] >= 18 and p[2] >= 80, personen)

result = list(map(lambda p: {"name": p[0], "age": p[1], "score": p[2]}, gefiltert))

print(result)
