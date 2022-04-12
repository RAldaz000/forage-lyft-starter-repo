from abc import ABC

class Tires(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def needs_service(self) -> bool:
        pass