import uuid
from demand import DemandProducer

class User(DemandProducer):
    def __init__(self, base_cost: int, cost_fluctuations: tuple) -> None:
        super().__init__(base_cost, cost_fluctuations)

    def __repr__(self) -> str:
        return f"{self.current_cost}"
    
    def copy(self):
        return User(
            self.base_cost,
            (self.fluctuation_min, self.fluctuation_max)
        )

class UserCluster:
    def __init__(self, users: dict) -> None:
        self.users = users
        self.uuid = uuid.uuid4()

    def update_demand(self) -> None:
        for user in self.users.values():
            user: User
            user.update_demand()

    def get_size(self) -> int:
        return len(self.users)

    def get_demand(self) -> int:
        total = 0
        for user in self.users.values():
            user: User
            total += user.get_demand()
        return total
    
    def __repr__(self) -> str:
        string = f"Cluster {self.uuid} - BEGIN\n"
        for id, user in self.users.items():
            user: User
            string += f"User {id} - current demand = {user}\n"
        string += f"Cluster {self.uuid} - END\n"
        return string
    
    @classmethod
    def from_nsized_equal_users(cls, template_user: User, n: int):
        users = dict()
        for i in range(n):
            users[i] = template_user.copy()
        return cls(
            users
        )
