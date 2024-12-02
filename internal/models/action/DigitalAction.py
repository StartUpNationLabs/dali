from Action import Action
from brick.Actuator import Actuator
from Signal import Signal

class DigitalAction(Action):
    def __init__(self, actuator: Actuator, value: Signal):
        super().__init__(actuator)
        self.value = value