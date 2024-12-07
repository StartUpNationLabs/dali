from models.action.Action import Action
from models.brick.Buzzer import Buzzer

class MelodyAction(Action):
    def __init__(self, actuator: Buzzer, frequency: int, duration: int = None):
        super().__init__()
        self.actuator = actuator
        self.frequency = frequency
        self.duration = duration
    
    def __str__(self) -> str :        
        return f"""\ttone({self.actuator.name}, {self.frequency}{', '+str(self.duration) if self.duration is not None else ''});
\tdelay({self.duration});
"""