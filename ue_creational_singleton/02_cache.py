# Goal: Design a Cache class using the Singleton pattern to store and retrieve key-value pairs globally across the
# application.
#
# Explanation: A cache system needs to be a single instance to ensure that all operations on the cache are
# centralized and consistent. This exercise tests the ability to implement a Singleton pattern to avoid duplicate
# caches which can lead to inefficient memory use and inconsistent data retrieval.







if __name__ == '__main__':
    cache1 = Cache()
    cache2 = Cache()
    cache1.add("key1", "value1")
    cache2.add("key2", "value2")

    print(cache1 == cache2)  # Should output: True
    print(cache1.get("key1"))  # Should output: "value1"
    print(cache2.get("key2"))  # Should output: "value2"
    print(cache1.get("key2"))  # Should also be able to retrieve "value2", proving shared instance
