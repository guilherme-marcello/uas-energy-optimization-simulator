from user import User, UserCluster
from network import NetworkZone, Gateway
from uas import UAV
from geolocation import Position, Circle
from random import randint


class World:
    def __init__(self, uavs: dict, network_zones: dict, regions: dict) -> None:
        """
        Initializes a World with UAVs, network zones, and geographical regions.

        Args:
        - uavs (dict): A dictionary of UAVs in the world.
        - network_zones (dict): A dictionary of network zones in the world.
        - regions (dict): A dictionary of geographical regions in the world.
        """
        self.uavs = uavs
        self.network_zones = network_zones
        self.regions = regions
        self.instant = 0

    def switch(self, uav1: UAV, uav2: UAV):
        """
        Perform a handover of serving zones between two UAVs.

        Args:
        - uav1 (UAV): The first UAV.
        - uav2 (UAV): The second UAV.
        """
        uav1.handover(uav2)

    def advance(self, verbose=False) -> None:
        """
        Advance the simulation to the next time step, updating demand and managing resources.

        Args:
        - verbose (bool, optional): Whether to print detailed information during the advancement (default is False).
        """
        if verbose: print(f"t={self.instant} Advancing....")
        for network_zone in self.network_zones.values():
            network_zone: NetworkZone
            network_zone.update_demand()

        for zone_name, zone in self.network_zones.items():
            zone: NetworkZone
            if verbose: print(f"NetworkZone {zone_name} is now demanding {zone.get_demand()} for its {zone.cluster.get_size()} users.")

        for uav in self.uavs.values():
            uav: UAV
            demand = uav.get_current_demand()
            if verbose: print(f"Demand for UAV {uav.name} is {demand}.... current level is {uav.current_resource_level}")
            if not uav.supress_demand(demand) and verbose:
                print(f"FAILED TO SUPRESS DEMAND!!!!!")

        self.instant += 1


    def __repr__(self) -> str:
        """
        Returns a string representation of the World, including UAVs, network zones, and regions.

        Returns:
        - str: A string representing the World and its components.
        """
        string = "World - BEGIN\n"
        string += f"{self.uavs.values()}\n{self.network_zones.values()}"
        string += "World - END\n"
        return string
            

class World1(World):
    default_user = User(
        base_cost=10,
        cost_fluctuations=(-3,3)
    )

    REGIONS = {
        "A": Circle(center=Position(x=2, y=2)),
        "B": Circle(center=Position(x=4, y=6)),
        "C": Circle(center=Position(x=5, y=2))
    }


    NETWORK_ZONES = dict()
    for zone_name in "ABC":
        NETWORK_ZONES[zone_name] = NetworkZone(
            name=zone_name,
            region=REGIONS.get(zone_name), 
            cluster=UserCluster.from_nsized_equal_users(
                template_user=default_user, n=randint(1,3)
            )
        )

    UAVS = dict()
    for network_zone_name in "ABC":
        UAVS[network_zone_name] = UAV(
            name=f"networker_{network_zone_name}",
            battery_level=randint(20, 140),
            serving_zone=NETWORK_ZONES.get(network_zone_name)
        )

    uav_A: UAV = UAVS["A"]
    uav_B: UAV = UAVS["B"]
    uav_C: UAV = UAVS["C"]

    Gateway.create(
        _from=UAVS["A"], _to=UAVS["B"]
    )

    Gateway.create(
        _from=UAVS["B"], _to=UAVS["C"]
    )

    def __init__(self) -> None:
        super().__init__(World1.UAVS, World1.NETWORK_ZONES, World1.REGIONS)

class World2(World):
    default_user = User(
        base_cost=5,
        cost_fluctuations=(0, 0)
    )

    REGIONS = {
        "A": Circle(center=Position(x=2, y=2)),
        "B": Circle(center=Position(x=4, y=6)),
        "C": Circle(center=Position(x=5, y=2))
    }


    NETWORK_ZONES = dict()
    for zone_name in "ABC":
        NETWORK_ZONES[zone_name] = NetworkZone(
            name=zone_name,
            region=REGIONS.get(zone_name), 
            cluster=UserCluster.from_nsized_equal_users(
                template_user=default_user, n=ord(zone_name) % 64
            )
        )

    UAVS = dict()
    for network_zone_name in "ABC":
        UAVS[network_zone_name] = UAV(
            name=f"networker_{network_zone_name}",
            battery_level=ord(network_zone_name) * (5 - (ord(network_zone_name) % 64)) + (100*(ord(network_zone_name) % 2)) ,
            serving_zone=NETWORK_ZONES.get(network_zone_name)
        )

    uav_A: UAV = UAVS["A"]
    uav_B: UAV = UAVS["B"]
    uav_C: UAV = UAVS["C"]

    Gateway.create(
        _from=UAVS["A"], _to=UAVS["B"]
    )

    Gateway.create(
        _from=UAVS["B"], _to=UAVS["C"]
    )

    def __init__(self) -> None:
        super().__init__(World2.UAVS, World2.NETWORK_ZONES, World2.REGIONS)