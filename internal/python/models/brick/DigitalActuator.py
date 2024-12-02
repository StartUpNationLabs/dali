from models.brick.Actuator import Actuator

class DigitalActuator(Actuator):
    def __init__(self, name: str, pin: int):
        super().__init__(name,pin)