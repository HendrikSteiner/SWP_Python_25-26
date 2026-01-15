class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung
        self.abteilung.mitarbeiter.append(self) #direkt eintragen bei erstellung


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht, abteilung)
        if abteilung.leiter is not None:
            raise ValueError("Abteilung hat bereits einen Leiter!")
        abteilung.leiter = self


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []


    def abteilung_hinzufuegen(self, abteilung):
        self.abteilungen.append(abteilung)


    def anzahl_mitarbeiter(self):
        return sum(len(a.mitarbeiter) for a in self.abteilungen)

    def anzahl_abteilungsleiter(self):
        return sum(1 for a in self.abteilungen if a.leiter is not None)

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def abteilung_mit_meisten_mitarbeitern(self):
        anz = [len(a.mitarbeiter) for a in self.abteilungen] #liste mit den anz der mitarbeitern
        meisten = max(anz) #nimmt gößten Wert aus dieser liste
        index = anz.index(meisten) #gibt stelle von diesm größten Wert
        return self.abteilungen[index]

    def geschlechteranteil(self):
        alle = [m for a in self.abteilungen for m in a.mitarbeiter]
        gesamt = len(alle)
        frauen = sum(1 for m in alle if m.geschlecht == "w")
        maenner = gesamt - frauen
        return frauen * 100 / gesamt, maenner * 100 / gesamt



if __name__ == "__main__":
    firma = Firma("Steiner GmbH")

    it = Abteilung("IT")
    prod = Abteilung("PR")

    firma.abteilung_hinzufuegen(it)
    firma.abteilung_hinzufuegen(prod)

    it_leiter = Abteilungsleiter("Hendrik", "m", it)
    prod_leiter = Abteilungsleiter("Bob", "m", prod)

    m1 = Mitarbeiter("Julian", "w", it)
    m2 = Mitarbeiter("David", "m", it)
    m3 = Mitarbeiter("Eva", "w", prod)
    m4 = Mitarbeiter("Seppe", "m", prod)
    m5 = Mitarbeiter("Anna", "w", prod)
    m6 = Mitarbeiter("Claudia", "w", prod)
    m7 = Mitarbeiter("Jeff", "m", prod)

    print("Mitarbeiter gesamt:", firma.anzahl_mitarbeiter())
    print("Abteilungsleiter gesamt:", firma.anzahl_abteilungsleiter())
    print("Abteilungen gesamt:", firma.anzahl_abteilungen())

    groesste = firma.abteilung_mit_meisten_mitarbeitern()
    if groesste:
        print("Größte Abteilung:", groesste.name)

    frauen, maenner = firma.geschlechteranteil()
    print(f"Frauen: {frauen:.1f} %, Männer: {maenner:.1f} %")
