# Goal: Implement a ResourceAllocator class that manages allocation of unique resources such as IDs or network
# connections, ensuring that no resource is allocated more than once.
#
# Explanation: Resource allocation often requires central management to avoid conflicts, such as two processes using
# the same resource. The Singleton pattern ensures that all resource allocation requests are handled by a single
# instance, which maintains a record of all allocated resources and prevents duplication.






if __name__ == '__main__':
    allocator1 = ResourceAllocator()
    allocator2 = ResourceAllocator()
    res1 = allocator1.allocate_resource()
    res2 = allocator2.allocate_resource()

    print(allocator1 == allocator2)  # Should output: True
    print(res1 != res2)  # Should output: True, demonstrating unique resource allocation
    print(allocator1.list_resources())  # Should list resources including res1 and res2
