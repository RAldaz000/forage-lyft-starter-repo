from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self,engine):
        self.engine = engine

    def needs_service(self):
        return self.engine.needs_service()
