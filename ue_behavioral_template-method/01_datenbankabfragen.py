"""
Übung 1 - Datenbankabfragen

Das Template-Methoden-Muster kann verwendet werden, um eine Abfragevorlage zu erstellen,
deren spezifische Schritte dann in Subklassen implementiert werden können, falls erforderlich.

Implementieren Sie die Klassen 'DatabaseQuery', 'MySQLQuery' und 'PostgreSQLQuery'.
"""


class DatabaseQuery:
    pass


class MySQLQuery(DatabaseQuery):
    pass


class PostgreSQLQuery(DatabaseQuery):
    pass


if __name__ == "__main__":
    mysql_query = MySQLQuery()
    mysql_query.run("SELECT * FROM users")
    postgres_query = PostgreSQLQuery()
    postgres_query.run("SELECT * FROM users")