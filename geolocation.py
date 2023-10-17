class Position:
    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a Position object with the given coordinates.

        Args:
        - x (int): The x-coordinate of the position.
        - y (int): The y-coordinate of the position.
        """
        self.x = x
        self.y = y

    def distance_to(self, other) -> float:
        """
        Calculate the Euclidean distance between this position and another.

        Args:
        - other (Position): Another Position object to calculate the distance to.

        Returns:
        - float: The Euclidean distance between this position and the other position.
        """
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**.5

class Circle:
    def __init__(self, center: Position, radius: int = 1) -> None:
        """
        Initializes a Circle object with a center Position and an optional radius.

        Args:
        - center (Position): The Position object representing the center of the circle.
        - radius (int, optional): The radius of the circle (default is 1).
        """
        self.center = center
        self.radius = radius

    def get_center(self) -> Position:
        """
        Get the center Position of the circle.

        Returns:
        - Position: The Position object representing the center of the circle.
        """
        return self.center