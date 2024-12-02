from Actuator import Actuator

class Digital(Actuator):
    def __init__(self, name: str, pin: int):
        super().__init__(name,pin)