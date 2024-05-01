# Implement a bridge pattern that allows the same application data to be stored in different types of databases (
# e.g., SQL, NoSQL, In-Memory).

# Scenario: Modern applications might require different types of databases depending on the operations performed—SQL
# databases for complex queries, NoSQL for scalability with unstructured data, or in-memory for speed.
#
# Explanation: The Bridge pattern decouples the application’s data management operations from the specifics of
# various database technologies. This allows developers to implement data persistence that can easily adapt to
# different storage requirements or switch databases as scalability and performance needs evolve.






if __name__ == '__main__':
    sql_storage = SQLStorage()
    nosql_storage = NoSQLStorage()

    user_data_manager = UserDataManager(sql_storage)
    user_data_manager.store({"name": "Alice", "age": 30})

    user_data_manager.switch_storage(nosql_storage)
    user_data_manager.store({"name": "Bob", "age": 25})
