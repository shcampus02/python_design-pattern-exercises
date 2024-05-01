# Create a system that abstracts the management of resources like cloud services or hardware interfaces (e.g., AWS,
# Azure, On-Premise Hardware).


# Scenario: Enterprises that utilize cloud services often operate across multiple platforms, such as AWS or Azure,
# and may also manage on-premise hardware. Each platform has its own API and management tools, requiring different
# handling.

# Explanation: The Bridge pattern facilitates a uniform interface to manage these resources, abstracting away the
# specifics of each service provider or hardware interface. This setup enables seamless resource allocation and
# management across different environments, allowing system administrators and developers to interact with a
# consistent interface regardless of the underlying platform specifics.








if __name__ == '__main__':
    aws_resource_manager = AWSResourceManager()
    azure_resource_manager = AzureResourceManager()

    resource_coordinator = ResourceCoordinator(aws_resource_manager)
    resource_coordinator.allocate_resources("Compute", 5)

    resource_coordinator.switch_manager(azure_resource_manager)
    resource_coordinator.allocate_resources("Storage", 10)
