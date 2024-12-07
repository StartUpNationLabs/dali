from models.action.Action import Action
from models.brick.DigitalActuator import DigitalActuator
from models.Signal import Signal

class DigitalAction(Action):
    def __init__(self, actuator: DigitalActuator, value: Signal):
        super().__init__()
        self.actuator = actuator
        self.value = value
    
    def __str__(self) -> str :
        return f'\tdigitalWrite({self.actuator.name},{self.value.name});'