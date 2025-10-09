# SWP_Python_25-26

zum Video: https://www.youtube.com/watch?v=fM4O9bModsE&t=13s

type Hinting --> Datentypen werden nur für Klarheit hinzugefügt zB. firstname : str oder am ende der Methode ) -> dict: um fremden Nutzern des Codes
                zu zeigen das ein Directory returned wird; es ist aber nur zur Übersicht da also wenn ich jetzt in age : int einen String schreibe zB. "seven" wird dieser trotzedem 
                als String ausgegeben obwohl er kein int ist. 

type checking --> selbe vorgehensweise nur wird hier mithilfe eines Add-Ons (MyPy) kontrolliert ob die Eingabe auch wirklich dem Datentyp entspricht. Aber es wird nur 
                  im Code angezeigt als Hinweis, wenn man aber den Code ausführt kann immer noch ein int "seven" sein.

Data Validation --> im Gegensatz zu type checking hilft dir Data Validation wirklich bei Problemen im Code, sodass keine falschen Inputs gliefert werden.
                    (Validation Errors) zählt die Fehler; mit if not isinstance(first_name : str): raise TypeError("first_name must be a string") 
                    können solche Fehler abgefangen werden. -> Manuel Validation (Problem: viel Code selber schreiben)
                    import validate_call mit @validate_call aufrufen -> automatische Validation mit dem Vorteil das zB auch ein "38" als int 38 erkannt wird.

ArrayListe --> fixxe größe ein Array --> wenn dieses voll ist wird ein neues Array erstellt mir der doppelten Größe und das alte Array wird in das neue kopiert und 
                das alte wird wieder freigegeben. Garbage Collection --> gibt im Hintergrund automatisch 
liste --> verschiedene Datentypen in einer Liste
array --> fix vorgegebene Größe -> nicht erweiterbar; schneller als ArrayListe

Dictionary ->Key/Value paar; Mischung aus Array und Listen
list comprehensions -> vereifnachte, schönere Schreibweise eines Codeteils

aufgabe: 3 arten von list comprehension (lit, set, dict)
