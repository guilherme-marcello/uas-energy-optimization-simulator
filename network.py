from user import UserCluster
from geolocation import Circle

class NetworkZone:
    def __init__(self, name: str, region: Circle, cluster: UserCluster, gateway = None) -> None:
        """
        Initializes a NetworkZone with a name, geographical region, UserCluster, and optional gateway.

        Args:
        - name (str): The name of the network zone.
        - region (Circle): The geographical region defined as a Circle.
        - cluster (UserCluster): The UserCluster associated with the network zone.
        - gateway (optional): An optional gateway device for the network zone (default is None).
        """
        self.name = name
        self.region = region
        self.cluster = cluster
        self.gateway = None

    def get_demand(self) -> int:
        """
        Get the total demand from the UserCluster within the network zone.

        Returns:
        - int: The total demand from the UserCluster in this network zone.
        """
        return self.cluster.get_demand()
    
    def update_demand(self) -> None:
        """
        Update the demand for the UserCluster within the network zone.
        """
        self.cluster.update_demand()

    def __repr__(self) -> str:
        """
        Returns a string representation of the NetworkZone, including its name and UserCluster information.

        Returns:
        - str: A string representing the NetworkZone and its UserCluster.
        """
        return f"NetworkZone {self.name} - BEGIN\n{self.cluster}NetworkZone {self.name} - END\n"
    

class InterconnectedDevice:
    def __init__(self) -> None:
        """
        Initializes an InterconnectedDevice with incoming and outgoing connections.
        """
        self.incoming_devices = list()
        self.outgoing_device = None

    def add_incoming_device(self, device):
        """
        Add an incoming device to this InterconnectedDevice.

        Args:
        - device: Another InterconnectedDevice to be added as an incoming device.
        """
        self.incoming_devices.append(device)

    def remove_incoming_device(self, device):
        """
        Remove an incoming device from this InterconnectedDevice.

        Args:
        - device: Another InterconnectedDevice to be removed from incoming devices.
        """
        self.incoming_devices.remove(device)
    
    def set_outgoing_device(self, device):
        """
        Set the outgoing device for this InterconnectedDevice.

        Args:
        - device: Another InterconnectedDevice to be set as the outgoing device.
        """
        self.outgoing_device = device


class Gateway:
    @staticmethod
    def create(_from: InterconnectedDevice, _to: InterconnectedDevice):
        """
        Create a gateway connection between two InterconnectedDevices.

        Args:
        - _from (InterconnectedDevice): The InterconnectedDevice where the connection starts.
        - _to (InterconnectedDevice): The InterconnectedDevice where the connection ends.
        """
        _from.set_outgoing_device(_to)
        _to.add_incoming_device(_from)
