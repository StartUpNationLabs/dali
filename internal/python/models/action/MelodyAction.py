from models.action.Action import Action
from models.brick.Buzzer import Buzzer

class MelodyAction(Action):
    def __init__(self, actuator: Buzzer, frequency: int, duration: int = None):
        super().__init__()
        self.actuator = actuator
        self.frequency = frequency
        self.duration = duration
    
    def __str__(self) -> str :
        if (self.duration is None):
            return f"analogWrite({self.actuator.pin}, {self.frequency})"        
        return f"""\ttone({self.actuator.pin}, {self.frequency}, {self.duration});
\tdelay({self.duration});
"""