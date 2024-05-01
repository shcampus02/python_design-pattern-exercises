# Erstellen Sie eine Klasse PrivateDocument und einen SecureProxy, um die Zugriffskontrolle auf die `read`-Methode der Klasse PrivateDocument zu verwalten.
# Der SecureProxy sollte den Zugriff auf die `read`-Methode nur dann ermöglichen, wenn ein gültiges Passwort bereitgestellt wird.






if __name__ == '__main__':
    doc = SecureProxy(PrivateDocument("Geheimdokument"))
    doc.read("falsches Passwort")  # Sollte einen Fehler ausgeben
    doc.read("richtiges Passwort")  # Sollte den Inhalt des Dokuments ausgeben
