from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carriganTires import CarriganTires
from tires.octoprimeTires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_date : datetime, last_service_date : datetime, current_mileage : int, last_service_mileage : int , tire_wear : list) -> Car :
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date), CarriganTires(tire_wear))

    @staticmethod
    def create_glissade(current_date : datetime, last_service_date : datetime, current_mileage : int, last_service_mileage : int , tire_wear : list) -> Car :
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date), CarriganTires(tire_wear))

    @staticmethod
    def create_palindrome(current_date : datetime, last_service_date : datetime, warning_light_is_on : bool , tire_wear : list) -> Car :
        return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(current_date, last_service_date), CarriganTires(tire_wear))

    @staticmethod
    def create_rorschach(current_date : datetime, last_service_date : datetime, current_mileage : int, last_service_mileage : int , tire_wear : list) -> Car :
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date), OctoprimeTires(tire_wear))

    @staticmethod
    def create_thovex(current_date : datetime, last_service_date : datetime, current_mileage : int, last_service_mileage : int , tire_wear : list) -> Car :
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date), OctoprimeTires(tire_wear))
