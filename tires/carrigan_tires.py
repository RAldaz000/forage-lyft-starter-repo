from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear : list):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return max(self.tire_wear) >= 0.9
