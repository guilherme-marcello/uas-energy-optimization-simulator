import uuid
from demand import DemandProducer

class User(DemandProducer):
    def __init__(self, base_cost: int, cost_fluctuations: tuple) -> None:
        """
        Initializes a User with a base cost and cost fluctuations.

        Args:
        - base_cost (int): The initial cost of the demand.
        - cost_fluctuations (tuple): A tuple containing the minimum and maximum values for cost fluctuations.
        """
        super().__init__(base_cost, cost_fluctuations)

    def __repr__(self) -> str:
        """
        Returns a string representation of the User.

        Returns:
        - str: A string representing the current demand cost of the User.
        """
        return f"{self.current_cost}"
    
    def copy(self):
        """
        Creates a copy of the User with the same base cost and cost fluctuations.

        Returns:
        - User: A new User object with the same characteristics.
        """
        return User(
            self.base_cost,
            (self.fluctuation_min, self.fluctuation_max)
        )

class UserCluster:
    def __init__(self, users: dict) -> None:
        """
        Initializes a UserCluster with a dictionary of users.

        Args:
        - users (dict): A dictionary where keys are user IDs and values are User objects.
        """
        self.users = users
        self.uuid = uuid.uuid4()

    def update_demand(self) -> None:
        """
        Update the demand of all users within the cluster.
        """
        for user in self.users.values():
            user: User
            user.update_demand()

    def get_size(self) -> int:
        """
        Get the size of the UserCluster, which is the number of users in the cluster.

        Returns:
        - int: The number of users in the cluster.
        """
        return len(self.users)

    def get_demand(self) -> int:
        """
        Calculate the total demand from all users within the cluster.

        Returns:
        - int: The total demand from all users in the cluster.
        """
        total = 0
        for user in self.users.values():
            user: User
            total += user.get_demand()
        return total
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the UserCluster, including user information.

        Returns:
        - str: A string representing the UserCluster and its users.
        """
        string = f"Cluster {self.uuid} - BEGIN\n"
        for id, user in self.users.items():
            user: User
            string += f"User {id} - current demand = {user}\n"
        string += f"Cluster {self.uuid} - END\n"
        return string
    
    @classmethod
    def from_nsized_equal_users(cls, template_user: User, n: int):
        """
        Creates a UserCluster with a specified number of equal template users.

        Args:
        - template_user (User): A User object to serve as a template for creating users in the cluster.
        - n (int): The number of users to create in the cluster.

        Returns:
        - UserCluster: A new UserCluster with the specified number of users, all based on the template_user.
        """
        users = dict()
        for i in range(n):
            users[i] = template_user.copy()
        return cls(
            users
        )
