"""
Übung 3 - Browser Verlauf

In diesem Beispiel implementieren Sie ein einfacher Browser Verlauf, der das Memento-Muster nutzt.

Implementieren Sie die Klassen 'Browser', 'BrowserState' und 'BrowserHistory'.
"""


class Browser:
    pass


class BrowserState:
    pass


class BrowserHistory:
    pass


if __name__ == "__main__":
    browser = Browser()
    browser_history = BrowserHistory()
    browser.open_website("http://google.com")
    browser.open_website("http://example.com")
    browser_history.add_history(browser.save_state())
    browser.open_website("http://anotherexample.com")
    browser.restore_state(browser_history.get_last_visited())