#1) Gegeben ist eine Liste mit Zahlen von 1 bis 30. Erstelle eine neue Liste, die nur die Zahlen enthält,
# die durch 3 teilbar sind. Für jedes Element soll in der neuen Liste auch ein Text
# angehängt werden (z.B. "ist durch 3 teilbar" oder "nicht teilbar") – aber nur die Zahlen, die teilbar sind,
# sollen drin sein.
numbers = [number for number in range(1, 31) if number % 3 == 0]
print(numbers)

#2) Set-Aufgabe:
# Du bekommst einen Text mit mehreren Wörtern und möchtest alle einzigartigen Wörter, die länger als
# 4 Buchstaben sind, herausfiltern. Erstelle mit einer Set Comprehension eine Menge dieser Wörter,
# die die Länge > 4 haben.
# Zusätzlich: Prüfe in der Comprehension ob ein Wort auch das Zeichen "s" enthält
# – nur solche Wörter sollen in das Set.
text = "Python ist eine sehr mächtige Programmiersprache und ermöglicht schnelle Entwicklung von Software in jeder Umgebung"
words = {word for word in text.split() if len(word) > 4 and "s" in word}
print(words)

#3) Dictionary-Aufgabe:
# Gegeben ist ein Dictionary, in dem Namen von Schülern (Keys) und ihre Punktzahl im Test (Values) stehen.
# Erstelle ein neues Dictionary, in dem Schüler mit mindestens 50 Punkten den Status "Bestanden" erhalten
# und alle anderen "Nicht bestanden".
# Nutze dazu eine Dictionary Comprehension mit if/else, um die Statuswerte zu setzen.
points = {
    "Anna": 65,
    "Ben": 48,
    "Clara": 75,
    "David": 32,
    "Eva": 50
}
status = {students: ("Bestanden" if points[students] >= 50 else "Nicht bestanden") for students in points}
print(status)