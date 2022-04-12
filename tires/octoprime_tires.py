from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear : list):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3.0
