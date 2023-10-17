from random import randint

class DemandProducer:
    def __init__(self, base_cost: int, cost_fluctuations: tuple) -> None:
        """
        Initializes a DemandProducer.

        Args:
        - base_cost (int): The initial cost of the demand.
        - cost_fluctuations (tuple): A tuple containing the minimum and maximum values for cost fluctuations.
        """
        self.base_cost = base_cost
        self.current_cost = self.base_cost
        self.fluctuation_min, self.fluctuation_max = cost_fluctuations
        self.fluctuation = lambda: randint(self.fluctuation_min, self.fluctuation_max)

    def update_demand(self) -> None:
        """
        Updates the demand cost by applying a random fluctuation within the specified range.

        If the updated cost falls below 0, it is reset to the base cost.
        """
        self.current_cost += self.fluctuation()
        if self.current_cost < 0:
            self.current_cost = self.base_cost

    def get_demand(self) -> int:
        """
        Get the current demand cost.

        Returns:
        - int: The current demand cost.
        """
        return self.current_cost
    
class DemandConsumer:
    def __init__(self, resource: int) -> None:
        """
        Initializes a DemandConsumer with a given resource level.

        Args:
        - resource (int): The initial resource level of the consumer.
        """
        self.current_resource_level = resource

    def get_resource_level(self) -> int:
        """
        Get the current resource level of the consumer.

        Returns:
        - int: The current resource level.
        """
        return self.current_resource_level

    def supress_demand(self, demand: int) -> bool:
        """
        Attempt to suppress demand by consuming resources.

        Args:
        - demand (int): The demand to be suppressed.

        Returns:
        - bool: True if the demand was successfully suppressed (resource level remains non-negative), False otherwise.
        """
        self.current_resource_level -= demand
        return self.current_resource_level >= 0
    
    def alive(self) -> bool:
        """
        Check if the consumer is still alive, i.e., if it has a positive resource level.

        Returns:
        - bool: True if the consumer has a positive resource level, indicating it is still alive; otherwise, False.
        """
        return self.current_resource_level > 0
