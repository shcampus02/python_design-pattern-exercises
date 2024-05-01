"""
Übung 3 - Log Event Handler

In einer Logging Anwendung sollten verschiedene Arten von Log-Events unterschiedlich gehandhabt werden. Beispielsweise
könnten INFO Logs nur in einer Datei gespeichert werden, während ERROR Logs zusätzlich per Email an die
Systemadministrator*innen gesendet werden.

Implementieren Sie eine Kette der Verantwortung, bei der jedes Glied in der Kette für eine bestimmte Log-Ebene und die
entsprechende Behandlung verantwortlich ist. Erstellen Sie die Klassen InfoLogger, WarningLogger und ErrorLogger.
"""


class AbstractLogger:
    # Platz für Ihre Implementierung
    pass


class InfoLogger(AbstractLogger):
    # Platz für Ihre Implementierung
    pass


class WarningLogger(AbstractLogger):
    # Platz für Ihre Implementierung
    pass


class ErrorLogger(AbstractLogger):
    # Platz für Ihre Implementierung
    pass


if __name__ == "__main__":
    # Hier sind einige vordefinierte Tests. Erweitern Sie Ihre Implementierung so, dass sie diese Tests bestehen.
    log_chain = InfoLogger(WarningLogger(ErrorLogger()))

    # Test 1
    assert log_chain.handle("INFO") == "Logging INFO"
    # Test 2
    assert log_chain.handle("WARNING") == "Logging WARNING"
    # Test 3
    assert log_chain.handle("ERROR") == "Logging ERROR"
    # Test 4
    assert log_chain.handle("UNKNOWN") == "Invalid log level"
