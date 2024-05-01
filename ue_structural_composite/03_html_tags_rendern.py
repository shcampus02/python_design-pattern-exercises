"""
Übung 3 - HTML-Tags rendern

In dieser Übung erstellen Sie eine Struktur, um HTML-Tags zu rendern. Ein HTML-Tag hat einen Tag-Namen und kann
entweder ein Eltern-Tag sein, der Kinder-Tags enthält, oder ein Blatt-Tag ohne Kinder. Beide Arten von HTML-Tags sollen
sich selbst in HTML-Form rendern können.

Implementieren Sie die Klassen `LeafHTMLTag` und `ParentHTMLTag`.
"""


class HTMLTag:
    pass

class LeafHTMLTag(HTMLTag):
    pass

class ParentHTMLTag(HTMLTag):
    pass

if __name__ == "__main__":
    # Hier sind einige vordefinierte Tests. Erweitern Sie Ihre Implementierung so, dass sie diese Tests bestehen.
    leaf = LeafHTMLTag("br")
    parent = ParentHTMLTag("p")
    parent.add(leaf)

    # Test 1
    assert leaf.render() == "<br />"
    # Test 2
    assert parent.render() == "<p><br /></p>"
