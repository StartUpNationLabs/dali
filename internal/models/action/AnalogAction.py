from Action import Action
from brick.Actuator import Actuator

class AnalogAction(Action):
    def __init__(self, actuator: Actuator, frequency: int, duration: int = None):
        super().__init__(actuator)
        self.frequency = frequency
        self.duration = duration