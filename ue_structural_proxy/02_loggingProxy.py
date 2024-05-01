# Erstelle eine Klasse Database und einen LoggingProxy, um den Aufruf der `insert`-Methode zu überwachen.
# Der LoggingProxy sollte einen Log-Eintrag erstellen, wann und mit welchen Daten die `insert`-Methode aufgerufen wurde.






if __name__ == '__main__':
    db = LoggingProxy(Database())
    db.insert("Neuer Datenbankeintrag")  # Sollte einen Log-Eintrag erstellen und den Eintrag in die Datenbank einfügen
