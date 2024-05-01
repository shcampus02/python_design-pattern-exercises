"""
Übung 4 - Abteilungsstruktur einer Firma

In dieser Übung sollen Sie die Hierarchie einer Firma darstellen, die aus verschiedenen Abteilungen besteht.
Jede Abteilung kann Mitarbeiter oder auch Unterabteilungen beinhalten. Es gibt zwei Arten von Mitarbeitern: Manager und
Entwickler. Jeder Mitarbeiter hat einen Namen und ein Gehalt.

Implementieren Sie die Klassen `Manager`, `Developer` und `Department`.
"""


class OrganizationalComponent:
    pass


class Employee(OrganizationalComponent):
    pass

class Manager(Employee):
    pass

class Developer(Employee):
    pass

class Department(OrganizationalComponent):
    pass

if __name__ == "__main__":
    # Hier sind einige vordefinierte Tests. Erweitern Sie Ihre Implementierung so, dass sie diese Tests bestehen.
    manager = Manager("Manager", 5000)
    developer = Developer("Developer", 4000)
    department = Department("Engineering")
    department.add(manager)
    department.add(developer)

    # Test 1
    assert manager.get_salary() == 5000
    # Test 2
    assert developer.get_salary() == 4000
    # Test 3
    assert department.get_salary() == 9000
