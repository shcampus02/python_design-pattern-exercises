# Erstellen Sie eine Klasse WebService und einen CachingProxy, um die Daten, die von der `getData`-Methode der Klasse WebService abgerufen wurden, zwischenzuspeichern.
# Der CachingProxy sollte die Daten zwischenspeichern und bei wiederholtem Aufruf der Methode mit denselben URL-Parametern die zwischengespeicherten Daten zurückgeben.






if __name__ == '__main__':
    service = CachingProxy(WebService())
    service.getData("http://example.com")  # Sollte den Webaufruf durchführen und das Ergebnis zwischenspeichern
    service.getData("http://example.com")  # Sollte das zwischengespeicherte Ergebnis zurückgeben
