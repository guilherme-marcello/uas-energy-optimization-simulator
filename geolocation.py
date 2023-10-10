class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**.5

class Circle:
    def __init__(self, center: Position, radius: int = 1) -> None:
        self.center = center
        self.radius = radius

    def get_center(self) -> Position:
        return self.center