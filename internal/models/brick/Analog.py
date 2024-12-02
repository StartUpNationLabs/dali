from Actuator import Actuator

class Analog(Actuator):
    def __init__(self, name: str, pin: int):
        super().__init__(name,pin)