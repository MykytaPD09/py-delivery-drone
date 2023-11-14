class Cargo:
    def __init__(
            self,
            weight: int
    ) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords=None
    ) -> None:
        self.name: str = name
        self.weight: int = weight
        self.coords: list[int] = coords if (
                coords is not None) else [0, 0]

    def go_forward(
            self,
            step: int = 1
    ) -> None:
        self.coords[1] += step

    def go_back(
            self,
            step: int = 1
    ) -> None:
        self.coords[1] -= step

    def go_right(
            self,
            step: int = 1
    ) -> None:
        self.coords[0] += step

    def go_left(
            self,
            step: int = 1
    ) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return (f"Robot: {self.name}, "
                f"Weight: {self.weight}")


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords=None,
            coordsthird=None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        if coordsthird is None:
            coordsthird = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.coordsthird: list[int] = coordsthird

    def go_up(
            self,
            step: int = 1
    ) -> None:
        self.coordsthird[2] += step
        self.coords = (self.coords[:2]
                       + [self.coordsthird[2]])

    def go_down(
            self,
            step: int = 1
    ) -> None:
        self.coordsthird[2] -= step
        self.coords = (self.coords[:2]
                       + [self.coordsthird[2]])


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords=None,
        coordsthird=None,
        max_load_weight: int = 0,
        current_load=None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        if coordsthird is None:
            coordsthird = [0, 0, 0]
        super().__init__(name, weight,
                         coords, coordsthird)
        self.max_load_weight: int = max_load_weight
        self.current_load: Cargo = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if (self.current_load is None
                and cargo.weight <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
