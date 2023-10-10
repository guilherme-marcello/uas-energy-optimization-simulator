from user import UserCluster
from geolocation import Circle




class NetworkZone:
    def __init__(self, name: str, region: Circle, cluster: UserCluster, gateway = None) -> None:
        self.name = name
        self.region = region
        self.cluster = cluster
        self.gateway = None

    def get_demand(self) -> int:
        return self.cluster.get_demand()
    
    def update_demand(self) -> None:
        self.cluster.update_demand()

    def __repr__(self) -> str:
        return f"NetworkZone {self.name} - BEGIN\n{self.cluster}NetworkZone {self.name} - END\n"
    

class InterconnectedDevice:
    def __init__(self) -> None:
        self.incoming_devices = list()
        self.outgoing_device = None

    def add_incoming_device(self, device):
        self.incoming_devices.append(device)
    
    def set_outgoing_device(self, device):
        self.outgoing_device = device


class Gateway:
    @staticmethod
    def create(_from: InterconnectedDevice, _to: InterconnectedDevice):
        _from.set_outgoing_device(_to)
        _to.add_incoming_device(_from)
