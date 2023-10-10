from random import randint

class DemandProducer:
    def __init__(self, base_cost: int, cost_fluctuations: tuple) -> None:
        self.base_cost = base_cost
        self.current_cost = self.base_cost
        self.fluctuation_min, self.fluctuation_max = cost_fluctuations
        self.fluctuation = lambda: randint(self.fluctuation_min, self.fluctuation_max)

    def update_demand(self) -> None:
        self.current_cost += self.fluctuation()
        if self.current_cost < 0:
            self.current_cost = self.base_cost

    def get_demand(self) -> int:
        return self.current_cost
    
class DemandConsumer:
    def __init__(self, resource: int) -> None:
        self.current_resource_level = resource

    def get_resource_level(self) -> int:
        return self.current_resource_level

    def supress_demand(self, demand: int) -> bool:
        self.current_resource_level -= demand
        return self.current_resource_level >= 0
    
    def alive(self) -> bool:
        return self.current_resource_level > 0
