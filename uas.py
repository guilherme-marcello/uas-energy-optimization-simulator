from demand import DemandConsumer
from network import InterconnectedDevice, NetworkZone


class UAV(DemandConsumer, InterconnectedDevice):
    def __init__(self, name: str, battery_level: int, serving_zone: NetworkZone = None) -> None:
        """
        Initializes a UAV (Unmanned Aerial Vehicle) with a name, battery level, and an optional serving zone.

        Args:
        - name (str): The name of the UAV.
        - battery_level (int): The initial battery level of the UAV.
        - serving_zone (NetworkZone, optional): The optional serving zone that the UAV is associated with (default is None).
        """
        DemandConsumer.__init__(self, resource=battery_level)
        InterconnectedDevice.__init__(self)
        self.serving_zone = serving_zone
        self.name = name

    def attach_to(self, zone: NetworkZone):
        """
        Attach the UAV to a specified NetworkZone.

        Args:
        - zone (NetworkZone): The NetworkZone to which the UAV will be attached.
        """
        self.serving_zone = zone

    def get_serving_zone_demand(self) -> int:
        """
        Get the demand from the serving zone, if the UAV is associated with one.

        Returns:
        - int: The demand from the serving zone, or 0 if not associated with any serving zone.
        """
        return self.serving_zone.get_demand() if self.serving_zone else 0

    def get_current_demand(self) -> int:
        """
        Calculate the total demand on the UAV, considering both the serving zone and incoming devices.

        Returns:
        - int: The total demand on the UAV.
        """
        demand_from_incoming_devices = 0
        for uav in self.incoming_devices:
            uav: UAV
            demand_from_incoming_devices += uav.get_current_demand()

        total = self.get_serving_zone_demand() + demand_from_incoming_devices
        #print(f"Total demand for UAV {self.name} is {total} ({self.get_serving_zone_demand()} + {demand_from_incoming_devices})")
        return total
    
    def handover(self, other):
        """
        Perform a handover of the serving zone and connections with another UAV.

        Args:
        - other (UAV): Another UAV with which the handover is being performed.
        """
        source_zone = self.serving_zone
        self.serving_zone = other.serving_zone
        other.serving_zone = source_zone

        source_incoming_devices = []
        for incoming_device in self.incoming_devices:
            incoming_device: InterconnectedDevice = incoming_device
            self.remove_incoming_device(incoming_device)
            source_incoming_devices.append(incoming_device)

        sink_incoming_devices = []
        for incoming_device in other.incoming_devices:
            incoming_device: InterconnectedDevice = incoming_device
            other.remove_incoming_device(incoming_device)
            sink_incoming_devices.append(incoming_device)

        # update gateways
        source_gateway = self.outgoing_device
        if source_gateway:
            source_gateway.remove_incoming_device(self)
            source_gateway.add_incoming_device(other)

        sink_gateway = other.outgoing_device
        if sink_gateway:
            sink_gateway.remove_incoming_device(other)
            sink_gateway.add_incoming_device(self)
        
        self.outgoing_device = other.outgoing_device
        other.outgoing_device = source_gateway

        # update incoming devices
        for device in sink_incoming_devices:
            device: InterconnectedDevice = device
            self.add_incoming_device(device)
            device.set_outgoing_device(self)
        for device in source_incoming_devices:
            device: InterconnectedDevice = device
            other.add_incoming_device(device)
            device.set_outgoing_device(other)

    def __repr__(self) -> str:
        """
        Returns a string representation of the UAV, including its name, battery level, serving zone, incoming devices, and outgoing device.

        Returns:
        - str: A string representing the UAV and its attributes.
        """
        string = f"UAV {self.name} "
        string += f"- battery {self.current_resource_level} "
        string += f"- serving zone {self.serving_zone.name} "
        string += f"- in{[uav.name for uav in self.incoming_devices]} "
        string += f"- out[{self.outgoing_device.name if self.outgoing_device else None}]\n"
        return string
    
