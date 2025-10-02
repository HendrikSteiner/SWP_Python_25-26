# if / if else
x = 10
if x > 5:
    print("x ist größer als 5")
elif x == 5:
    print("x ist gleich 5")
else:
    print("x ist 5 oder kleiner")

# for Schleife
for i in range(3):  # i läuft von 0 bis 2
    print("for:", i)

# while Schleife
count = 0
while count < 3:
    print("while:", count)
    count += 1

# break und continue in Schleife
for i in range(5):
    if i == 3:
        break    # Schleife wird bei i==3 beendet
    if i == 1:
        continue # überspringt den Rest der Schleife bei i==1
    print("loop:", i)

# Beispiel für Parsing
data = "123"
number = int(data)  # Parse String zu Integer
print("Parsed Number:", number)

# try-except-else-finally Konstrukt
try:
    x = int("abc")  # führt zu ValueError
except ValueError:
    print("Fehler: keine Zahl")
else:
    print("Kein Fehler, x =", x)
finally:
    print("Dieser Block wird immer ausgeführt")
